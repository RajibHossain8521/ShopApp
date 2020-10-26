

def login_validation(password):
    """ Function : For verifying user password """
    with open("C:\\Users\\HP\\Desktop\\ShopApp\\shop_manager\\shop\\login.txt", "r+") as log:
        check_password = log.read()
        if check_password == password:
            return True
        else:
            return False

if __name__ == "__main__":
    login_validation(12345)
