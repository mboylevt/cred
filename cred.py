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
from lib import StudentLib, DBConnect, RecordLib, RecordTypeLib, ClassLib
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


### Student Routes
@app.route('/_student/get_student_names')
def get_student_names():
    """
    Retrieve a list of the student names from the DB.
    """
    first_name = request.args.get('firstName', 0, type=str)
    students = StudentLib.find_students(session=session, first_name=first_name)
    to_return = {}
    for student in students:
        to_return[student.id] = student.first_name + ' ' + student.last_name
    return jsonify(result=to_return)


@app.route('/_student/get_cred_points_by_type')
def get_cred_points_by_type():
    """
    Get cred points by studentId
    """
    student_id = request.args.get('studentId', 0, type=str)
    records = RecordLib.get_records_per_student(session=session, student_id=student_id)
    record_types = RecordTypeLib.get_record_types(session=session)
    record_type_tracker = {}
    to_return = {}
    points_earned = {}
    points_missed = {}
    for record_type in record_types:
        record_type_tracker[record_type.id] = record_type.letter
        points_missed[record_type.letter] = 0
        points_earned[record_type.letter] = 0
    for record in records:
        index = record_type_tracker[record.record_type_id]
        if record.score == 1:
            points_earned[index] += 1
        else:
            points_missed[index] += 1
    to_return['Earned'] = points_earned
    to_return['Missed'] = points_missed
    return jsonify(result=to_return)

@app.route('/_student/get_cred_points_by_class')
def get_cred_points_by_class():
    """
    Get cred points by studentId

    Returns a json array, with both points awarded and points missed
    """
    student_id = request.args.get('studentId', 0, type=str)
    records = RecordLib.get_records_per_student(session=session, student_id=student_id)
    classes = ClassLib.get_classes(session=session)
    class_tracker = {}
    to_return = {}
    points_earned = {}
    points_missed = {}
    for klass in classes:
        class_tracker[klass.id] = klass.name
        points_earned[klass.name] = 0
        points_missed[klass.name] = 0
    for record in records:
        index = class_tracker[record.class_id+1]
        if record.score == 1:
            points_earned[index] += 1
        else:
            points_missed[index] += 1
    to_return['Earned'] = points_earned
    to_return['Missed'] = points_missed
    return jsonify(result=to_return)

### Main Route
@app.route('/')
def home():
    return render_template('search_students.html', students=[])

if __name__ == '__main__':
    app.run(debug=True, port=5050)
