from flask import jsonify


def ping():
    return jsonify({
        'result': 'pong'
    })
