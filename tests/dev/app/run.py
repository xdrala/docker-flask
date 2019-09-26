from flask import Flask, make_response, jsonify

app = Flask('docker-flask:dev')


@app.route('/', methods=['GET'])
def root():
    return make_response(
        jsonify({'message': 'Hello from Flask', 'env': 'dev-reload'}))
