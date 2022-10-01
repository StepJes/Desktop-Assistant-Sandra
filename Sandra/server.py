from concurrent.futures import process
from flask import Flask, request, make_response, jsonify
from flask_cors import CORS
import subprocess

# from main import main

app = Flask(__name__)
CORS(app)


@app.route("/on", methods=['GET'])
def on():
    response = make_response(
        jsonify(
            {"message": 'running'}
        ),
        200,
    )
    response.headers["Content-Type"] = "application/json"

    global process
    process = subprocess.call(["python", "main.py"])

    return response


@app.route("/off", methods=['GET'])
def off():
    response = make_response(
        jsonify(
            {"message": 'running'}
        ),
        200,
    )
    response.headers["Content-Type"] = "application/json"
    # print(process)
    process.terminate()

    return response


if __name__ == "__main__":
    app.run(debug=True)
