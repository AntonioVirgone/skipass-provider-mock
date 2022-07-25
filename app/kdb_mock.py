import json

import flask
from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/api/services/thirdparty/tx/typeA/', methods=['POST'])
def create_with_response_200():
    serviceCode = request.json['serviceCode']

    if serviceCode == 100:
        print(str(request.json['serviceCode']))
        return json.dumps({
            "id": "KDB_806FF566-24C7-4BA1-8CB5-D53CE1828B00",
            "idCode": "2022-05-03",
            "currency": "EUR",
            "serviceCode": "33",
            "merchantOrderId": "aaaa",
            "amount": 1000,
            "status": "PRENOTATA",
            "creationDate": 1651575401731,
            "updateDate": 1651575401543,
            "plateNumber": "AB728JK",
            "countryCode": "HR",
            "statusDescription": "PRENOTATA",
            "recorded": False,
            "rejected": False,
            "terminalId": "",
            "pointOfService": {
                "code": "3327",
                "address": "Valtournenche",
                "agreementCode": 3932,
                "upperAgreementCode": "3932",
                "serviceCode": "33",
                "serviceCounterpartCode": "26019260",
                "externalPointOfService": "24",
                "description": "Valtournenche",
                "upperAgreementName": "CERVINO SPA",
                "agreementName": "CERVINO SPA",
                "description2": "SKIDATA",
                "description1": "Skipass - Valtournenche"
            },
            "details": [],
            "attachments": [],
            "startTime": 1651575401000
        })
    elif serviceCode == 400:
        return flask.Response(status=403, response=json.dumps(
            {"code": "REQUEST_BOOKING_KAA_READ_TIMEOUT", "description": "Lorem ipsum"}))
    elif serviceCode == 500:
        return flask.Response(status=403,
                              response=json.dumps({"code": "ENTRY_NOT_FOUND", "description": "Lorem ipsum"}))
    elif serviceCode == 600:
        return flask.Response(status=403, response=json.dumps(
            {"code": "REQUEST_BOOKING_KAA_NOT_AUTHORIZED_ERROR_204", "description": "Lorem ipsum"}))
    elif serviceCode == 700:
        return flask.Response(status=403, response=json.dumps(
            {"code": "REQUEST_BOOKING_KAA_NOT_AUTHORIZED_ERROR_205", "description": "Lorem ipsum"}))
    elif serviceCode == 800:
        return flask.Response(status=403, response=json.dumps(
            {"code": "REQUEST_BOOKING_KAA_NOT_AUTHORIZED_ERROR_211", "description": "Lorem ipsum"}))
    elif serviceCode == 900:
        return flask.Response(status=403, response=json.dumps(
            {"code": "REQUEST_BOOKING_KAA_NOT_AUTHORIZED_ERROR_599", "description": "Lorem ipsum"}))
    else:
        return flask.Response(status=400)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
