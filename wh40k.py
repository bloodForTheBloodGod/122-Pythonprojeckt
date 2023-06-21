import mysql.connector

cnx = mysql.connector.connect(user='root', password='root',
    host='localhost',
    database='warhammer40k')
cnx.close()
