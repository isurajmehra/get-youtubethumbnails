from flask import render_template, redirect, request, flash
from app import app
from main import get_youtube_thumbnail

@app.route('/')
def index():
    return render_template("index.html", title="Get YouTube Thumbnails")

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.form:
        yt_url = request.form['url_submit']
        images = get_youtube_thumbnail(yt_url)
    else:
        return redirect('/')

    if images:
        return render_template('submit.html', title='Your Youtube Thumbnails', images=images)
    else:
        flash("")
        return redirect('/')
