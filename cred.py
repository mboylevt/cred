# -*- coding: utf-8 -*-
"""
    Flaskr
    ~~~~~~

    A microblog reflection application written as Flask tutorial with
    Flask and sqlite3.

    :copyright: (c) 2014 by Armin Ronacher.
    :license: BSD, see LICENSE for more details.
"""

from flask import Flask, request, render_template, jsonify
from lib import StudentLib, DBConnect, RecordLib, RecordTypeLib
from flask.ext.assets import Environment, Bundle

app = Flask(__name__)
session = DBConnect.connect()

env = Environment(app)

# Bundle and register javascript and CSS
js_common = Bundle('js/jquery/jquery.js', output='gen/common.js')
js_student = Bundle('js/student/student.js', output='gen/student.js')
js_charts = Bundle('js/charts/charts.min.js','js/charts/credCharts.js',  output='gen/charts.js')
css_common = Bundle('css/style.css', output='gen/common.css')

env.register('js_common', js_common)
env.register('js_student', js_student)
env.register('js_charts', js_charts)
env.register('css_common', css_common)

@app.route('/_student/get_student_names')
def get_student_names():
    first_name = request.args.get('firstName', 0, type=str)
    students = StudentLib.find_students(session=session, first_name=first_name)
    to_return = {}
    for student in students:
        to_return[student.id] = student.first_name + ' ' + student.last_name
    return jsonify(result=to_return)


@app.route('/_student/get_cred_points_by_type')
def get_cred_point_by_type():
    student_id = request.args.get('studentId', 0, type=str)
    students = RecordLib.list_records_per_student(session=session, student_id=student_id)
    record_types = RecordTypeLib.get_record_types()
    to_return = {}
    for student in students:
        to_return[student.id] = student.first_name + ' ' + student.last_name
    return jsonify(result=to_return)


@app.route('/')
def home():
    return render_template('search_students.html', students=[])

if __name__ == '__main__':
    app.run(debug=True, port=5050)
