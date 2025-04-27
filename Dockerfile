FROM python:3.10-slim

WORKDIR /LLM_application_chatbot

COPY requirements.txt .

RUN pip install torch --index-url https://download.pytorch.org/whl/cpu

RUN grep -v '^torch' requirements.txt > reqs_no_torch.txt \
 && pip install --no-cache-dir -r reqs_no_torch.txt

ENV HF_HUB_REQUEST_TIMEOUT=120 \
    HF_HUB_DOWNLOAD_RETRY=5 \
    HF_HUB_ENABLE_EMERGENCY_RETRY=true \
    HF_HUB_EMERGENCY_RETRY_WAIT_TIME=10

RUN pip install --no-cache-dir huggingface_hub \
 && python - << 'EOF'

COPY . .

EXPOSE 5000
CMD ["python", "app.py"]
