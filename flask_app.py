# A very simple Flask Hello World app for you to get started with...

from flask import Flask

from validadoc import testeCPF
import os
from tempo import hora_atual

app = Flask(__name__)


@app.route('/')
def hello_world():
    # a = testeCPF()
    # return a + 'Hello from Flask!'

    return 'Hora atual: ' + str(hora_atual())

computerName = os.environ['COMPUTERNAME']
if __name__ == "__main__" and computerName == 'DESKTOP-91FQJAU':
    app.run()
