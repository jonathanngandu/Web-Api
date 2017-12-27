FROM python:3

EXPOSE 5000

RUN mkdir /app
WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install --upgrade pip setuptools
RUN pip install -r requirements.txt

COPY . /app

ENV PYTHONPATH $PYTHONPATH:./app/src
ENV GOOGLE_APPLICATION_CREDENTIALS=/app/src/myGoogle/creds/creds_2.json
ENV FLASK_DEBUG=1
ENV IMAGE_URL='https://storage.googleapis.com/images_11_12_17'

RUN chown -R www-data:www-data /app

ENTRYPOINT ["gunicorn", "-b", ":8080", "main:app"]