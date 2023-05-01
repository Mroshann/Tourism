from Travel import app
from flask import render_template,request,flash,redirect,url_for
from flask_login import login_user,login_required,logout_user
from . import db
from .models import User
from werkzeug.security import check_password_hash, generate_password_hash



username = dict()

@app.route('/',methods=['POST','GET'])
@app.route('/home/',methods=['POST','GET'])
def home_page():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        remember = True if request.form.get('remember') else False
        
        user = User.query.filter_by(email=email).first()
        
        if not user or not check_password_hash(user.password,password):
            flash('Please check your login details and try again.')
            return redirect(url_for('home_page'))
        
        login_user(user,remember = remember)
        username[1] = user.username
        return redirect(url_for('home_page'))
    if 1 in username.keys():
        name = username[1]
        return render_template('index.html',username=name)
    return render_template('index.html')
@app.route('/package')
# @login_required
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


@app.route('/signup',methods=['GET','POST'])
def signup():
    if request.method == "POST":
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')
        
        user = User.query.filter_by(email=email).first()
        
        if user:
            flash('Email address already exits')
            return redirect(url_for('auth.signup'))
        
        new_user = User(email =email,username= username,password=generate_password_hash(password,method='sha256'))
        
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('home_page'))

    return render_template('signup.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home_page'))

@app.route('/recommendation')
@login_required
def recommend():
    return redirect('http://localhost:8501')