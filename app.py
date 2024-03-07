from flask import Flask, render_template
import sqlite3
from sqlite3 import Error

DATABASE = "C:/Users/riley/OneDrive/DTS/13DTS/Flask/student grades"
app = Flask(__name__)


def create_connection(db_file):
    try:
        connection = sqlite3.connect(db_file)
        return connection
    except Error as e:
        print(e)
    return None


@app.route('/')
def hello_world():  # put application's code here
    return render_template('home.html')


@app.route('/student')
def hello_world():  # put application's code here
    con = create_connection(DATABASE)
    query = "SELECT id, Name, Last_name, Student_id, Email FROM Student_Names"
    cur = con.cursor()
    cur.execute(query)
    student_name = cur.fetchall()
    con.close()
    print(student_name)
    return render_template('student.html', students=student_name)


if __name__ == '__main__':
    app.run()
