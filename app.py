from flask import Flask, request, render_template
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from flask_cors import CORS
import json
import torch

app = Flask(__name__)
CORS(app)

model_name = "facebook/blenderbot-400M-distill"
model = AutoModelForSeq2SeqLM.from_pretrained(
    model_name,
    from_tf=True,
    from_flax=False,
    cache_dir=None,
    force_download=False,
    ignore_mismatched_sizes=False,
    local_files_only=False,
    revision="main",
    use_safetensors=None,
    torch_dtype=torch.float16,
    low_cpu_mem_usage=True,
    trust_remote_code=True
)
tokenizer = AutoTokenizer.from_pretrained(model_name)
conversation_history = []

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/chatbot', methods=['POST'])
def handle_prompt():
    data = request.get_data(as_text=True)
    data = json.loads(data)
    input_text = data['prompt']

    history = "\n".join(conversation_history)
    inputs = tokenizer.encode_plus(history, input_text, return_tensors="pt")
    outputs = model.generate(**inputs, max_length= 60)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()

    conversation_history.append(input_text)
    conversation_history.append(response)

    return response

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
