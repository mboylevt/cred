# -*- coding: utf-8 -*-
"""
    Flaskr
    ~~~~~~

    A microblog example application written as Flask tutorial with
    Flask and sqlite3.

    :copyright: (c) 2014 by Armin Ronacher.
    :license: BSD, see LICENSE for more details.
"""

from flask import Flask, request, redirect, url_for, render_template, flash
from lib import StudentLib, DBConnect


app = Flask(__name__)
session = DBConnect.connect()

@app.route('/student/search', methods=['POST'])
def student_search():
    first_name = request.form['first-name']
    students = StudentLib.find_students(session=session, first_name=first_name)
    return render_template('search_students.html', students=students)

@app.route('/')
def search_students(students=[]):
    # students = StudentLib.get_students(session)
    return render_template('search_students.html', students=students)

if __name__ == '__main__':
    app.run(debug=True)
