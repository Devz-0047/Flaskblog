from flask import Blueprint, render_template, url_for, flash, redirect
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User
from flaskblog import bcrypt, db
main = Blueprint('main', __name__)
from flask_login from login_user

posts = [
    {
        'author': "Deven Grey",
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2028'
    },
    {
        'author': 'Ionic Dane',
        'title': "Blog Post 2",
        'content': 'Second post content',
        'date_posted': 'April 23, 2041'
    }
]

@main.route("/")
@main.route("/home")
def home():
    return render_template('home.html', posts=posts)

@main.route("/about")
def about():
    return render_template('about.html', title="About")

@main.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data,email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@main.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,form.password.data):
            login_user(user,form.remember.data)
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful, please check email and password')
    return render_template('login.html', title='Login', form=form)
