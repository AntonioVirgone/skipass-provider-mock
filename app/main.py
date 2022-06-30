import flask
from flask import Flask

app = Flask(__name__)


@app.route('/<provider>/login', methods=['POST'])
def enable(provider, cardCode):
    print(f'Mock enable request to {provider} by card {cardCode}')

    status_code = flask.Response(status=201, response="helloworld")
    return status_code


@app.route('/<provider>/card/<cardCode>/abilitation', methods=['POST'])
def enable(provider, cardCode):
    print(f'Mock enable request to {provider} by card {cardCode}')

    if int(cardCode) <= 900:
        status_code = flask.Response(status=403)
    else:
        status_code = flask.Response(status=201)
    return status_code


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
