import smtplib
import ssl
import random
import hashlib
import re
import psycopg2


def validate_email_address(email_address):
    # CHECK VALID EMAIL ADDRESS
    return re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email_address)


def reset_code_mail(email_address):
    reset_code = ''.join(random.sample('0123456789ABCDEF', 6))
    code = reset_code
    # Ecrypte the reset code
    reset_code = reset_code.encode()
    encrypted_code = hashlib.sha224(reset_code).hexdigest()

    # WRITE RESET CODE INFO DATABASE TABLE FOR OWNER
    try:
        connection = psycopg2.connect(
            database='shop_management', 
            user='postgres', 
            password='12345',
            port='5432')

        cursor = connection.cursor()
        encrypted_code = str(encrypted_code)
        sql = ('''UPDATE owner_info SET verification_code='%s' WHERE sl=0''') % encrypted_code
        cursor.execute(sql)
        connection.commit()
        connection.close()

        port = 465  # SSL
        smtp_server = "smtp.gmail.com"
        sender_email = "testmail8521@gmail.com"
        receiver_email = email_address
        password = "developer@123mail"

        subject = "ShopApp - Password Reset Mail"
        body = "Hello Sir,\n\nSet your new PASSWORD with this validation code: " + \
            code + "\n\nThank you."

        message = 'Subject: {}\n\n{}'.format(subject, body)

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
            return True
    except:
        print("Fail")
        return False

def verify_reset_password_code(verify_code, new_password):
    # READ VERIFICATION CODE FROM DATABASE
    try:
        connection = psycopg2.connect(
            database='shop_management', 
            user='postgres', 
            password='12345',
            port='5432')

        cursor = connection.cursor()
        cursor.execute('''SELECT * FROM owner_info''')
        result = cursor.fetchone()
        verification_code = result[1]
    
        verify_code = verify_code.encode()
        encrypted_code = hashlib.sha224(verify_code).hexdigest()
        
        if verification_code == str(encrypted_code):
            new_password = str(new_password).encode()
            encrypted_password = hashlib.sha224(new_password).hexdigest()
            encrypted_password = str(encrypted_password)
            sql = ('''UPDATE owner_info SET password='%s' WHERE sl=0''') % encrypted_password
            cursor.execute(sql)
            sql = ('''UPDATE owner_info SET verification_code='' WHERE sl=0''')
            cursor.execute(sql)
            connection.commit()
            connection.close()
            return True
        else:
            # Invalid Authentication Code
            return False
    except:
        return False


# if __name__ == "__main__":
#     verify_reset_password_code("2EAC0F", 4321)
#     #reset_code_mail('rajibhossain8521@gmail.com')
