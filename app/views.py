"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

from app import app, db
from flask import render_template, request, jsonify, send_file
import os
from flask_wtf.csrf import generate_csrf
from werkzeug.utils import secure_filename
import os
from app.models import Movie
from app.forms import MovieForm


###
# Routing for your application.
###

@app.route('/')
def index():
    return jsonify(message="This is the beginning of our API")


###
# The functions below should be applicable to all Flask apps.
###

@app.route('/api/v1/movies', methods = ['POST'])
def movies():
    response = ''
    form = MovieForm()

    if form.validate_on_submit():
        
        title = form.title.data
        description = form.desc.data
        poster = form.poster.data
        
        poster_filename = secure_filename(poster.filename)
        
        response = jsonify({"message": "Movie Successfully added", 
                    "title": title,
                    "poster": poster_filename, 
                    "description": description})
            
        new_movie = Movie(title, description, poster_filename)
        poster.save(os.path.join(app.config['UPLOAD_FOLDER'], poster_filename))
    
        # adding to database
        db.session.add(new_movie)
        db.session.commit()
        
        return response
        
    else:
        errors = form_errors(form)
        
        if (errors):
            
            error_list = {"errors": []}
            
            error_list['errors'] = errors
            
            response = jsonify(error_list)
            
        return response
    
@app.route('/api/v1/csrf-token', methods=['GET']) 
def get_csrf():     
    return jsonify({'csrf_token': generate_csrf()}) 

# Here we define a function to collect form errors from Flask-WTF
# which we can later use
def form_errors(form):
    error_messages = []
    """Collects form errors"""
    for field, errors in form.errors.items():
        for error in errors:
            message = u"Error in the %s field - %s" % (
                    getattr(form, field).label.text,
                    error
                )
            error_messages.append(message)

    return error_messages

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404