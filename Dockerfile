FROM python:3.11-slim

COPY app ./app
COPY requirements.txt requirements.txt
COPY *.py ./
COPY .env ./.env


RUN python -m pip install --upgrade pip && pip install -r requirements.txt

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]