import hashlib

file_path = 'C:/Users/HP/Desktop/ShopApp/shop_manager/shop/'

def login_validation(password):
    """ Function : For verifying user password """
    with open(file_path + "login.txt", "r+") as log:
        check_password = log.read()

        password = str(password).encode()
        encrypted_password = hashlib.sha224(password).hexdigest()

        if check_password == encrypted_password:
            return True
        else:
            return False

#if __name__ == "__main__":
    #login_validation(1234)
