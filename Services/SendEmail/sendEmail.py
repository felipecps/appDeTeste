import math
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import json
from datetime import datetime



def send_email(body, subject, receiver):

    if os.name == 'nt':
        path_total = 'Services//SendEMail//config.json'
    else:
        path_total = '/home/felipecps/Git/appDeTeste/Services/SendEmail/config.json'

    with open(path_total, 'r') as f:
        data = json.load(f)

    message = body  # Type your message
    msg = MIMEMultipart()
    # password = data['pw'] + str(10 - 8 + 5 - 7) + str(8 % 12) + str(int(math.pow(36, 1 / 2))) + str(2 + 2)
    password = 'gixggorefcutddqq'

    if receiver == "felipePessoal":
        dest = data['eu'] + data['xavier'] + '@' + data['gmail']
    elif receiver == "felipeTrabalhoSs":
        dest = data['f'] + data['xavier'] + '@' + data['ss']
    elif receiver == "felipeTrabalhoSd":
        dest = data['f'] + data['xavier'] + '@' + data['sd']
    elif receiver == "fernandaPessoal":
        dest = data['fer'] + '.' + data['ramos'] + '@' + data['gmail']
    elif receiver == "fernandaTrabalho":
        dest = data['fer'] + '.' + data['ramos'] + '@' + data['k']

    msg['From'] = "contadeteste0@gmail.com"  # Type your own gmail address
    msg['To'] = dest  # Type your friend's mail address
    msg['Subject'] = subject  # Type the subject of your message
    msg.attach(MIMEText(message, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com: 587')
    server.starttls()
    server.login(msg['From'], password)
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()
    print("enviado para: ", dest)
