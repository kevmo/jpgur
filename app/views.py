from flask import render_template, request

from app import app

from models import Link, LinkService

links = LinkService()


@app.route('/')
def index():

    existing_links = links.
    
    return render_template('index.html', links=existing_links
    )


@app.route('/', methods=['POST'])
def successful_post():

    form = request.form

    link = form.get('link')

    l = Link(link)

    saved_link = links.save(l)

    print saved_link


    return  "trilla"