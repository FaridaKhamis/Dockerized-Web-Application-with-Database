
# Flask is used to create your application instance which will serve as the central object managing your web application.
# render_template lets you create a dynamic HTML response using a template file 
from flask import Flask, render_template
#  pymysql to connect to your MySQL database, execute SQL queries, and handle the data in your database.
import pymysql
# This line creates an instance of the Flask class.
#  The name argument is used to determine the root path of the application so that Flask can find resource files relative to the location of the application script.

app = Flask(__name__)

# Database connection info
DB_HOST = 'db'  # Name of the service in docker-compose
DB_USER = 'root'  # used to authenticate with the database        
DB_PASSWORD = 'rootpassword'     #password for the database user
DB_NAME = 'studentdb'      #name of the database to connect to.
#tells Flask that the home function should be called when a web browser requests the root URL of the web server.
@app.route('/')
def home():
    connection = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, db=DB_NAME)   #establish a connection to the MySQL database using the connection details specified earlier in your code.
    cursor = connection.cursor()    # creates a cursor object ( to execute queries and fetch results) using the connection
    cursor.execute("SELECT * FROM students")   #to retrieve all entries in the students table.
    students = cursor.fetchall()    #Fetches all the rows returned by the SQL query and stores them in the variable students
    cursor.close()       # Closes the cursor object after the query execution
    connection.close()     #Closes the connection to the database
    return render_template('index.html', students=students)    # renders an HTML template named index.html, passing the students data to the template
                                                               # Flask uses Jinja2 templating engine

#Execute the Flask application on the local development server at port 3000.
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
