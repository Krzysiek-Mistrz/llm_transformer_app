# LLM Application Chatbot

## Overview
A simple Flask-based web app that lets users chat with a pretrained Transformer model (e.g. BlenderBot).  
- **Frontend**: HTML/CSS/JavaScript  
- **Backend**: Flask + Hugging Face Transformers  
- **Model**: `facebook/blenderbot-400M-distill`

## Features
- User can send messages via a textarea form.  
- JavaScript handles form submission, displays a loading indicator, and appends AI responses to the chat window.  
- Backend routes user messages to the Transformer model and returns generated text.

## Prerequisites
- Python 3.8+  
- pip  
- (Optional) Virtual environment tool, e.g. `venv` or `conda`

## Installation

1. Clone the repo  
   ```bash
   git clone https://github.com/your-org/llm-chatbot.git
   cd llm-chatbot
   ```

2. Create and activate a virtual environment  
   ```bash
   python -m venv venv
   source venv/bin/activate    # on Windows: venv\Scripts\activate
   ```

3. Install Python dependencies  
   ```bash
   pip install -r requirements.txt
   ```

4. (Optional) Download static assets  
   Ensure `static/css/style.css`, `static/script.js`, and images (`user.jpeg`, `Bot_logo.png`, `Error.png`) exist.

## Project Structure
```
/
├── app.py                 # Flask application entrypoint
├── requirements.txt       # Python dependencies
├── templates/
│   └── index.html         # Single-page chat UI
├── static/
│   ├── css/
│   │   └── style.css      # Chat UI styling
│   ├── script.js          # Frontend messaging logic
│   ├── user.jpeg          # User avatar
│   ├── Bot_logo.png       # Bot avatar
│   └── Error.png          # Error icon
└── README.md              # Project documentation
```

## Usage

1. Run Flask:
   ```bash
   python app.py
   ```
2. Open your browser at `http://127.0.0.1:5000/`.

3. Start chatting!

## Backend Details
- **Route /**  
  Serves `index.html`.

- **Route /chatbot [POST]**  
  Expects JSON `{ "prompt": "<user message>" }`.  
  - Maintains a global `conversation_history` list.  
  - Concatenates history into a single string, tokenizes with `AutoTokenizer`, and generates a response.  
  - Returns raw text.  

### Improvements
- Import the tokenizer:  
  ```python
  from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
  ```
- Avoid duplicate `Flask(__name__)`.  
- Implement history truncation, e.g. only keep the last N exchanges.

## Frontend Details
- **script.js**  
  - Captures form submissions, displays messages in the DOM.  
  - Sends POST to `/chatbot` (update the URL).  
  - Uses dynamic elements for loading and error handling.  

## Troubleshooting
- **Model loading errors**: Ensure you have enough RAM or switch to a smaller model.  
- **CORS issues**: Already enabled via `flask_cors.CORS(app)`.  
- **Static file errors**: Verify `url_for('static', ...)` paths match your directory layout.

## License
MIT © JC