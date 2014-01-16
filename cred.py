# -*- coding: utf-8 -*-
"""
    Flaskr
    ~~~~~~

    A microblog example application written as Flask tutorial with
    Flask and sqlite3.

    :copyright: (c) 2014 by Armin Ronacher.
    :license: BSD, see LICENSE for more details.
"""

from flask import Flask, request, session, redirect, url_for, \
     render_template, flash


# create our little application :)
app = Flask(__name__)

@app.route('/')
def display_entries():
    return "CRED"

if __name__ == '__main__':
    app.run()
