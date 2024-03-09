# Importing module 
import mysql.connector as m

# Creating connection object
mydb = m.connect(
	host = "localhost",
	user = "root",
	password = "root@123",
 	auth_plugin = "mysql_native_password"
)

mycursor = mydb.cursor()
mycursor.execute("create database patient")
mycursor.execute("CREATE TABLE Add  (Reg No. Varchar(50) Primary key, First Name Varchar(20), Last Name(20), Gender ENUM('Male', 'Female', 'Other'), DOB VARCHAR(20), Contact_number VARCHAR(20), Registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP")


