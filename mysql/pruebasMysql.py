import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="seminario"
)

mycursor = mydb.cursor()

sql = "INSERT INTO detalle (id, tipo, color, otro) VALUES (%s,%s,%s,%s)"
val = (1,"carro","azul","rapido");

mycursor.execute(sql, val)

mydb.commit()
mydb.close()


print(mycursor.rowcount, "record inserted.")
