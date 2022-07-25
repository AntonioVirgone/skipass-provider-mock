import json

import flask
from flask import Flask
from flask import request


app = Flask(__name__)


@app.route('/<provider>/login', methods=['POST'])
def login(provider):
    global token, status_code

    if provider.upper() == "SKIDATA":
        token = "hello-" + str(provider)
        status_code = flask.Response(status=201, response=token)
    elif provider.upper() == "AXESS":
        token = {
            "token": "hello-" + str(provider)
        }
        status_code = flask.Response(status=201, response=json.dumps(token))

    return status_code


@app.route('/<provider>/card/<cardCode>/abilitation', methods=['POST'])
def disable(provider, cardCode):
    if int(cardCode) <= 900:
        status_code = flask.Response(status=403)
    else:
        status_code = flask.Response(status=201)
    return status_code


@app.route('/<provider>/card/<cardCode>/registration', methods=['POST'])
def disable(provider, cardCode):
    if int(cardCode) <= 900:
        status_code = flask.Response(status=403)
    else:
        status_code = flask.Response(status=201)
    return status_code


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
