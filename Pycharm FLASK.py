from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello Woer1ld!!!!!!!adsadasd!!'


if __name__ == '__main__':
    app.run()
