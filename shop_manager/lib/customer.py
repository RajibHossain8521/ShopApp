""" All functionalities for Customers related operations """
import psycopg2


def add_customer():
    # Add new customerf
    try:
        connection = psycopg2.connect(
            database='shop_management', 
            user='postgres', 
            password='12345',
            port='5432')

        cursor = connection.cursor()
        #cursor.execute("SELECT * FROM customer_info WHERE phone_number = %s", (contact_number,))
    except:
        return False
    finally:
        connection.close()


def customer_info(contact_number):
    # customer informations
    try:
        connection = psycopg2.connect(
            database='shop_management', 
            user='postgres', 
            password='12345',
            port='5432')
 
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM customer_info WHERE phone_number = %s", (contact_number,))

        result = cursor.fetchall()
        print(result)        
    
    except:
        return False
    finally:
        connection.close()


def customer_payment_info():
    pass


def customer_bazar_list():
    pass


def customer_periodic_bazar_list():
    pass


if __name__ == "__main__":

    customer_info('022')