# Importing module 
import mysql.connector as m

# Creating connection object
mydb = m.connect(
	host = "localhost",
	user = "root",
	password = "root@123",
	database = "patient",
 	auth_plugin = "mysql_native_password"
)

mycursor = mydb.cursor()
reg_name = input("Enter Registration number: ")
first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
gender = input("Enter patient's gender (Male/Female/Other): ")
dob = input("Enter date of birth: ")
contact_number = input("Enter patient's contact number: ")

