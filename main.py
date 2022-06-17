import flask
from flask import Flask

api = Flask(__name__)


@api.route('/<provider>/card/<cardCode>/abilitation', methods=['GET'])
def enable(provider, cardCode):
    print(f'Mock enable request to {provider} by card {cardCode}')

    if int(cardCode) <= 1000:
        status_code = flask.Response(status=403)
    else:
        status_code = flask.Response(status=201)
    return status_code


if __name__ == '__main__':
    api.run()
