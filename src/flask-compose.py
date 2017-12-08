from flask import Flask
from src.myGoogle.google_api import GoogleApi

app = Flask(__name__)


@app.route('/')
def hello_world():
  return 'Hello from Docker PyCharm!'

@app.route('/google')
def google():
  return GoogleApi().run()


if __name__ == '__main__':
  app.run(host='0.0.0.0')