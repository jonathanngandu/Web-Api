FROM python:3

EXPOSE 5000

RUN mkdir /app
WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install --upgrade pip setuptools
RUN pip install -r requirements.txt

COPY . /app

ENV PYTHONPATH $PYTHONPATH:./app/src
ENV GOOGLE_APPLICATION_CREDENTIALS=/app/src/myGoogle/creds.json

CMD python src/flask-compose.py