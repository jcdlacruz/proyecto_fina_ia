import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="seminario"
)

mycursor = mydb.cursor()

sqlInsertDetalle = "INSERT INTO detalle (id, tipo, color, otro) VALUES (%s, %s, %s, %s)"
val = ("2", "carro", "verde", "lento")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
