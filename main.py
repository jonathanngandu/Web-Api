from flask import Flask, request, abort, jsonify
from src.myGoogle.google_api import GoogleApi

app = Flask(__name__)


@app.route('/', methods=['GET'])
def homepage():
    """
    Homepage
    """
    return jsonify({'message': 'hello'})


@app.route('/echo', methods=['POST'])
def echo():
    """Simple echo service."""
    message = request.get_json().get('message', '')
    return jsonify({'message': message})


@app.route('/google', methods=['PUT', 'POST'])
def image_text():
    """
    Get google vision text
    """
    image_name = request.get_json().get('filename', '')
    app.logger.debug(image_name)
    # try:
    app.logger.debug('200')
    return jsonify({'image': GoogleApi().run(image_name, app)})
    # except:
    #     app.logger.debug('404')
    #     return abort(404)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
