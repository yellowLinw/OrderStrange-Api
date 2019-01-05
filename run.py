#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask import jsonify
from flask_exceptions import APIException

from app import create_app
from common.jwt import blacklist

app = create_app()

@app.errorhandler(APIException)
def handle_exceptions(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@app.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    jti = decrypted_token['jti']
    return jti in blacklist

def main():
    # server_ip = '0.0.0.0'
    # server_port = 8000

    # app.run(host=server_ip, port=server_port, debug=True)
    app.run(debug=True)


if __name__ == '__main__':
    main()
