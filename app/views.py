from flask import render_template, request, redirect, url_for

from app import app
from main.utility.scraper import get_images
from models import Link, LinkService

links = LinkService()


@app.route('/')
def index():

    existing_links = links.all()

    print existing_links
    
    return render_template('index.html', links=existing_links
    )


@app.route('/', methods=['POST'])
def successful_post():

    form = request.form

    link = form.get('link')

    og_link = get_images(link)

    l = Link(link, og_link)

    saved_link = links.save(l)

    print "SAVED LINK: ", saved_link

    return redirect('/')