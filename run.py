#!/usr/bin/python3
# -*- coding: utf-8 -*-

from app import create_app

app = create_app()


def main():
    server_ip = '0.0.0.0'
    server_port = 8000

    app.run(host=server_ip, port=server_port, debug=True)


if __name__ == '__main__':
    main()
