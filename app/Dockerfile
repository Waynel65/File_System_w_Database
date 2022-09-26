FROM python:3.9

# expose port 5000 since flask listens on port 5000
EXPOSE 5000 

WORKDIR /app

COPY requirements.txt .
COPY config.py .
COPY creds.py .
COPY database.py .
COPY app.py .

RUN pip install -r requirements.txt

ENV PYTHONPATH ${PYTHONPATH}:/app

CMD python3 app.py