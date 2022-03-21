from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    print('test')
    print('new test')
    print('kk test')
    return 'hello'