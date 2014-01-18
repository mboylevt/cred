# -*- coding: utf-8 -*-
"""
    Flaskr
    ~~~~~~

    A microblog example application written as Flask tutorial with
    Flask and sqlite3.

    :copyright: (c) 2014 by Armin Ronacher.
    :license: BSD, see LICENSE for more details.
"""

from flask import Flask, request, render_template, jsonify
from lib import StudentLib, DBConnect


app = Flask(__name__)
session = DBConnect.connect()

@app.route('/_add_numbers')
def add_numbers():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a + b)

@app.route('/_student/search')
def student_search():
    first_name = request.args.get('firstName', 0, type=str)
    students = StudentLib.find_students(session=session, first_name=first_name)
    to_return = []
    for student in students:
        to_return.append(student.first_name + ' ' + student.last_name)
    return jsonify(result=to_return)

@app.route('/')
def home():
    return render_template('search_students.html', students=[])

if __name__ == '__main__':
    app.run(debug=True)
