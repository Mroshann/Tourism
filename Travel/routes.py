from Travel import app
from flask import render_template

@app.route('/')
@app.route('/home/')
def home_page():
    return render_template('index.html')


@app.route('/package')
def package_page():
    return render_template('package.html')
    
@app.route('/services')
def services_page():
    return render_template('services.html')

@app.route('/gallery')
def gallery_page():
    return render_template('gallery.html')

@app.route('/reviews')
def reviews_page():
    return render_template('reviews.html')

@app.route('/contact')
def contact_page():
    return render_template('contact.html')