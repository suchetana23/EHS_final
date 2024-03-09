from flask import Flask, render_template, request
import mysql.connector as m

mydb = m.connect(
	host = "localhost",
	user = "root",
	password = "root@123",
	database = "patient",
 	auth_plugin = "mysql_native_password"
)

mycursor = mydb.cursor()

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        reg_no = request.form['reg_no']
        select_query = "SELECT * FROM patients WHERE reg_no = %s"
        mycursor.execute(select_query, (reg_no,))
        rows = mycursor.fetchone()
        data = {'first_name': rows[1], 'last_name': rows[2], 'gender': rows[3], 'dob': rows[4]} 
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
