import smtplib
import ssl
import random2
import hashlib

# reset code text file path
file_path = 'C:/Users/HP/Desktop/ShopApp/shop_manager/shop/'


def generate_reset_code(email_address):
    reset_code = ''.join(random2.sample('0123456789ABCDEFGHIJ', 6))
    code = reset_code
    # Ecrypte the reset code
    reset_code = reset_code.encode()
    encrypted_code = hashlib.sha224(reset_code).hexdigest()

    with open(file_path+"reset_code.txt", "w") as log:
        log.write(encrypted_code)

    send_reset_mail(code, email_address)


def send_reset_mail(code, email_address):

    port = 465  # SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "testmail8521@gmail.com"
    receiver_email = email_address
    password = "developer@123mail"

    subject = "Password Reset Mail"
    body = "Hello Sir,\n\nSet your new PASSWORD with this validation code: " + \
        code + "\n\nThank you."

    message = 'Subject: {}\n\n{}'.format(subject, body)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)


def verify_reset_password_code(verify_code, new_password):
    with open(file_path+"reset_code.txt", "r") as log:
        file_data = log.read()

    verify_code = verify_code.encode()
    encrypted_code = hashlib.sha224(verify_code).hexdigest()

    if file_data == encrypted_code:
        with open(file_path+'login.txt', 'w') as log:
            new_password = str(new_password).encode()
            encrypted_password = hashlib.sha224(new_password).hexdigest()
            log.write(encrypted_password)
        return True

    else:
        # print("Invalid Authentication Code")
        return False

if __name__ == "__main__":
    #generate_reset_code()
    verify_reset_password_code("9HF18C", 1234)
