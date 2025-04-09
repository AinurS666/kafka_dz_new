FROM python:3.10.2

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY .venv .

CMD ["python","app/main.py"]