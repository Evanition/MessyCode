FROM python:3.10
WORKDIR /app  # Now we are inside /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ .

CMD ["sh", "-c", "python main.py & tail -f /dev/null"]

