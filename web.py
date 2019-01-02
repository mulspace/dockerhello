#!/usr/bin/env python

from flask import Flask, jsonify
import socket
import os
import getpass

app = Flask(__name__)

def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()

    return ip

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return jsonify({
		'path': path,
		'hostname': socket.gethostname(),
		'ip': get_host_ip(),
		'uid': os.getuid(),
		'username': getpass.getuser(),
		'home': os.environ['HOME'],
	        'INSTANCE': os.getenv('INSTANCE', 'default')
		})

@app.route('/todo', methods=['GET'])
def get_tasks():
    return jsonify({'todo': "..."})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

