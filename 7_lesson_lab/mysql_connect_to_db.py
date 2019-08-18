import mysql.connector


def get_products():
    con = mysql.connector.connect(host='192.168.31.6', user='root', password='333333', database='for_test')
    cursor = con.cursor()
    cursor.execute(query, )
    print(cursor.fetchall())
    cursor.close()


query = "SELECT `product name`, price, title, description FROM product JOIN category ON product.category = category.id"


def new_products():
    con = mysql.connector.connect(host='192.168.31.6', user='root', password='333333', database='for_test')
    cursor = con.cursor()
    query = "INSERT INTO product VALUES (%s, %s, %s, %s)"
    values = (None, 'Carrot', 7.5, 1)
    cursor.execute(query, values)
    con.commit()
    cursor.close()
    con.close

new_products()
