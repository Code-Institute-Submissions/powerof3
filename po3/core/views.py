from flask import render_template


@core.route('/')
def index():
    return render_template('index.html')