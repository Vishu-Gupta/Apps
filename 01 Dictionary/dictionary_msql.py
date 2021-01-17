"""Program to connect to a remote DB and query for word & its meanings"""
import mysql.connector

con = mysql.connector.connect(
    user="ardit700_student",
    password="ardit700_student",
    host="108.167.140.122",
    database="ardit700_pm1database"
)

cursor = con.cursor()

word = input("Enter word : ")

query = cursor.execute(f"SELECT * FROM Dictionary WHERE Expression = '{word}'")
results = cursor.fetchall()

if results:
    for result in results:
        print(result[1])
else:
    print("This word doesn't exist")
