
# A very simple Flask Hello World app for you to get started with...

from flask import Flask

from validadoc import testeCPF

app = Flask(__name__)

@app.route('/')
def hello_world():
    a = testeCPF()
    return a + 'Hello from Flask!'