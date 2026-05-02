import sqlite3

connection = sqlite3.connect("First_BD")

main_cursor = connection.cursor()

# main_cursor.execute(
#     "CREATE TABLE PRODUCTS (NAME_ARTICLE VARCHAR(50), PRICE FLOAT, SECTION VARCHAR(50))"
# )
# main_cursor.execute("INSERT INTO PRODUCTS VALUES('RAQUETA', 15, 'DEPORTES')")
# various_products = [
#     ("MACETA", 8, "HOGAR"),
#     ("PELOTA", 10, "JUGUETES"),
#     ("PALA", 4, "HOGAR"),
# ]
# main_cursor.executemany("INSERT INTO PRODUCTS VALUES(?,?,?)", various_products)

main_cursor.execute("SELECT * FROM PRODUCTS")

view_products = main_cursor.fetchall()
print(view_products)


for product in view_products:
    print(f"Name: {product[0]}, Precio: ${product[1]}")

connection.commit()
connection.close()
