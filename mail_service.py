import smtplib, ssl
from email.message import EmailMessage
import os
from dotenv import load_dotenv

load_dotenv()

port = 465  # For SSL
password = os.getenv("GMAIL_PASS")
sender_email = os.getenv("SENDER")
receiver_emails = os.getenv("RECEIVER").split(',')

# TEST_EMAIL = EmailMessage()

# TST_CONTENT = """
# Hello, this is sent from python
# """

# TEST_EMAIL.set_content(TST_CONTENT)

# TEST_EMAIL['subject'] = "Prueba Python"
# TEST_EMAIL['to'] = receiver_email
# TEST_EMAIL['from'] = sender_email

# # Create a secure SSL context
# context = ssl.create_default_context()

# with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
#     server.login("prueba.proteccion.sgz@gmail.com", password)
#     server.send_message(TEST_EMAIL)
#     # TODO: Send email here


def send_fib_email(result_map):
    msg = EmailMessage()

    msg['subject'] = "Prueba Tecnica - Sebastian Giraldo Zuluaga"
    msg['from'] = sender_email

    body = f"""
    Hora de Generación de la serie: {result_map['generation_time']}

    Serie: {result_map['sequence']}
    
    """

    msg.set_content(body)

    # Create a secure SSL context
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login("prueba.proteccion.sgz@gmail.com", password)
        msg["to"] = receiver_emails
        server.send_message(msg)

