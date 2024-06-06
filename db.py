import mysql.connector

# MySQL sunucusu ile bağlantı kurma
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="visa-application"
)

# Bir cursor oluşturma
cursor = conn.cursor()


# Bağlantıyı kapatma
cursor.close()
conn.close()
