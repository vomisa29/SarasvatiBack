FROM python:3.10

RUN apt-get update && apt-get install -y glpk-utils

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt

CMD ["sh", "-c", "uvicorn src.main:app --host 0.0.0.0 --port $PORT"]
