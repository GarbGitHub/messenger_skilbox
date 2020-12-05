from flask import Flask

app = Flask(__name__)


@app.route('/ ')
def hello():
    return ('Hello World!')


@app.route('/status')
def status():
    return status

app.run()


