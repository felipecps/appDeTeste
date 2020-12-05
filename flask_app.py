import datetime
import uuid
import os
from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime

# from Services.SendEmail.sendEmail import send_email
from Services.SendEmail.sendEmail import send_email

BOOKS = [
    {
        'id': uuid.uuid4().hex,
        'title': 'On the Road',
        'author': 'Jack Kerouac',
        'read': True
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Harry Potter and the Philosopher\'s Stone',
        'author': 'J. K. Rowling',
        'read': False
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Green Eggs and Ham',
        'author': 'Dr. Seuss',
        'read': True
    }
]

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/envia_email', methods=['POST'])
def envia_email():
    body = request.args.get('text', '')
    subject = request.args.get('subject', '')
    if subject == '':
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        subject = "Lembrete enviado às: " + str(current_time)

    checked_emails = request.args.get('checked', '').split(',')
    for receiver in checked_emails:
        send_email(body, subject, receiver)
    return 'ok'

def remove_book(book_id):
    for book in BOOKS:
        if book['id'] == book_id:
            BOOKS.remove(book)
            return True
    return False

# 80 janela
# 38 m2
# Eduardo

# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@app.route('/hora_atual')
def hello_world():
    # a = testeCPF()
    # return a + 'Hello from Flask!'

    return 'Hora atual: ' + str(datetime.datetime.now().time())



@app.route('/books', methods=['GET', 'POST'])
def all_books():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        BOOKS.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'read': post_data.get('read')
        })
        response_object['message'] = 'Book added!'
    else:
        response_object['books'] = BOOKS
    return jsonify(response_object)


@app.route('/books/<book_id>', methods=['PUT', 'DELETE'])
def single_book(book_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        remove_book(book_id)
        BOOKS.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'read': post_data.get('read')
        })
        response_object['message'] = 'Book updated!'
    if request.method == 'DELETE':
        remove_book(book_id)
        response_object['message'] = 'Book removed!'
    return jsonify(response_object)

try:
    computerName = os.environ['COMPUTERNAME']
    if __name__ == "__main__" and computerName == 'DESKTOP-91FQJAU':
        app.run()
except KeyError:
    pass
