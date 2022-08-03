import json

import flask
from flask import Flask, Response
from flask import request

app = Flask(__name__)


@app.route('/api/uaa/oauth/token', methods=['POST'])
def login():
    return Response(json.dumps({
        "access_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzY29wZSI6WyIzcmRwYXJ0eSJdLCJlbmFibGVkU2VydmljZXMiOm51bGwsImV4cCI6MTY1NDcxNzgyMSwiYXV0aG9yaXRpZXMiOlsiS1RRX1NFUlZJQ0VTX1NVUFBPUlRfQ09OU1VNRVIiLCJOT1RJRklDQVRJT05TX0FQSV9DT05TVU1FUiIsIkJOTF9BUElfQ09OU1VNRVIiLCJBUC1DT05TVU1FUiJdLCJqdGkiOiI2ZmIxYmUwYy0zYzM0LTRjYjctYWE2Yy1iNjhjODc0YWNiYTYiLCJjbGllbnRfaWQiOiJ3aXNlLXNlcnZlciJ9.oTFnlNXoUSjNhJaZitcUOkPU6L_6q_wZFL3aE3SXpxQNfT_lJ5xC_gxakODRyo86gA5Gz451418vtlACts0j039jWEGH7CwRiYZhDR5DLvgQGlDO5pZ5LTWBqIeRc9iTljFomaK7e5cm6mV94jGh4XaHXYLo6ZRpZi2HhCTIBG-pfiWGgZEi5V8dNwmlID2s9ng26YxFtj77s2rX5Iw5BD29jwQKSds1Nv2H4RduBAPUGV__gGtVtDcJ2BGpjGDU71RAUlYgMvmxghb53bSBfKpmpp4OiAnLfUhx9TXhCWEGUel22hvl3fkNK_K4y819VQUi7Qnczb-0uLHBIBiMRA",
        "expires_in": 35999
    }), content_type='application/json')


@app.route('/api/services/thirdparty/tx/typeA/', methods=['POST'])
def create_transaction():
    serviceCode = int(request.json['serviceCode'])

    if serviceCode == 100 or serviceCode == 33:
        print(str(request.json['serviceCode']))
        return Response(json.dumps({
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
        }), content_type='application/json')
    elif serviceCode == 400:
        return flask.Response(status=403,
                              response=json.dumps({"code": 403, "message": "",
                                                   "details": {
                                                       "kdbErrorResponse": {"code": "REQUEST_BOOKING_KAA_READ_TIMEOUT",
                                                                            "description": "Lorem ipsum"}}}),
                              content_type='application/json')
    elif serviceCode == 500:
        return flask.Response(status=403,
                              response=json.dumps({"code": 403, "message": "",
                                                   "details": {"kdbErrorResponse": {"code": "ENTRY_NOT_FOUND",
                                                                                    "description": "Lorem ipsum"}}}),
                              content_type='application/json')
    elif serviceCode == 600:
        return flask.Response(status=403,
                              response=json.dumps({"code": 403, "message": "",
                                                   "details": {"kdbErrorResponse": {
                                                       "code": "REQUEST_BOOKING_KAA_NOT_AUTHORIZED_ERROR_204",
                                                       "description": "Lorem ipsum"}}}),
                              content_type='application/json')
    elif serviceCode == 700:
        return flask.Response(status=403,
                              response=json.dumps({"code": 403, "message": "",
                                                   "details": {"kdbErrorResponse": {
                                                       "code": "REQUEST_BOOKING_KAA_NOT_AUTHORIZED_ERROR_205",
                                                       "description": "Lorem ipsum"}}}),
                              content_type='application/json')
    elif serviceCode == 800:
        return flask.Response(status=403,
                              response=json.dumps({"code": 403, "message": "",
                                                   "details": {"kdbErrorResponse": {
                                                       "code": "REQUEST_BOOKING_KAA_NOT_AUTHORIZED_ERROR_211",
                                                       "description": "Lorem ipsum"}}}),
                              content_type='application/json')
    elif serviceCode == 900:
        return flask.Response(status=403,
                              response=json.dumps(
                                  {"code": 403, "message": "",
                                   "details": {
                                       "kdbErrorResponse": {"code": "REQUEST_BOOKING_KAA_NOT_AUTHORIZED_ERROR_599",
                                                            "description": "Lorem ipsum"}}}),
                              content_type='application/json')
    else:
        return flask.Response(status=400)


@app.route('/api/services/thirdparty/tx/typeA/<transaction>', methods=['DELETE'])
def delete_transaction(transaction):
    return flask.Response(status=200)


@app.route('/api-third-party/v1/users/profile/me/plafonds', methods=['GET'])
def get_plafond():
    return flask.Response(status=200)


@app.route('/api/services/thirdparty/tx/any/<transaction>', methods=['GET'])
def get_transaction(transaction):
    return Response(json.dumps({
        "id": "KDB_806FF566-24C7-4BA1-8CB5-D53CE1828B01",
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
    }), content_type='application/json')


@app.route('/api/services/thirdparty/tx/typeA/<transaction>/authorize', methods=['POST'])
def close_transaction(transaction):
    if transaction == 'KDB_806FF566-24C7-4BA1-8CB5-D53CE1828B00':
        return Response(json.dumps({
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
        }), content_type='application/json')
    else:
        return flask.Response(status=403,
                              response=json.dumps(
                                  {"code": 403, "message": "",
                                   "details": {
                                       "kdbErrorResponse": {"code": "REQUEST_BOOKING_KAA_NOT_AUTHORIZED_ERROR_599",
                                                            "description": "Lorem ipsum"}}}),
                              content_type='application/json')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
