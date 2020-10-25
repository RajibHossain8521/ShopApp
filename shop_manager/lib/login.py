

def login_validation(password):
    """ Function : For verifying user password """
    with open("C:\\Users\\HP\\Desktop\\ShopApp\\shop_manager\\shop\\login.txt", "r+") as log:
        check_password = log.read()
        print(check_password)    

if __name__ == "__main__":
    login(12345)
