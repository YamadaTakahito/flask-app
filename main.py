from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'BBBY'

@app.route('/ping')
def ping():
    return 'pong'


if __name__ == "__main__":
    app.run(port=8000, host='0.0.0.0')