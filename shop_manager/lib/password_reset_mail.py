import smtplib, ssl
import random2


def generate_reset_code():
    reset_code = ''.join(random2.sample('0123456789ABCDEFGHIJ', 6))
    print(reset_code)

def send_reset_mail():
    port = 465 # SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "testmail8521@gmail.com"
    receiver_email = "rajibhossain8521@gmail.com"
    password = "developer@123mail"

    subject = "Password Reset Mail"
    body = "Set your new PASSWORD."

    message = 'Subject: {}\n\n{}'.format(subject, body)


    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)


if __name__ == "__main__":
    generate_reset_code()