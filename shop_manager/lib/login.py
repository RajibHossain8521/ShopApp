import hashlib
import psycopg2


def login_validation(password):
    """ Function : For verifying user password """
    try:
        connection = psycopg2.connect(
            database='shop_management', 
            user='postgres', 
            password='12345',
            port='5432')

        cursor = connection.cursor()
        cursor.execute('''SELECT * FROM owner_info''')

        result = cursor.fetchone()
        check_password = result[2]

        password = str(password).encode()
        encrypted_password = hashlib.sha224(password).hexdigest()

        if check_password == encrypted_password:
            return True
        else:
            return False

    except:
        return False
    finally:
        connection.close()


# if __name__ == "__main__":
#     login_validation(4321)
