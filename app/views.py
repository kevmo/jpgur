from flask import render_template, request

from app import app


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def successful_post():

    form = request.form

    print "FORM: ", form.get('link')

    return  "trilla"