from flask import Blueprint, render_template, url_for, flash, redirect
from flaskblog.forms import RegistrationForm, LoginForm

main = Blueprint('main', __name__)

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
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('main.home'))
    return render_template('register.html', title='Register', form=form)

@main.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com':
            flash('You have been logged in!', 'success')
            return redirect(url_for('main.home'))
        else:
            flash('Login Unsuccessful. Please check your email and password.', 'danger')
    return render_template('login.html', title='Login', form=form)
