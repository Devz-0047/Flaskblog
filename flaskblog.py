
from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
from models import User, Post
app = Flask(__name__)
app.config['SECRET_KEY'] = '07f1441e22be6d53f289ec35f235fe6c'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # Corrected key name
db = SQLAlchemy(app)

# User model


# Example posts for testing
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

# Routes
@app.route("/")
@app.route("/home")
def home():  # Fixed method name from 'Home' to 'home' to match URL
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title="About")

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))  # Fixed typo 'Hfome' to 'home'
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com':  # Basic admin check
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check your email and password.', 'danger')
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    with app.app_context():
        db.create_all() 
    app.run(debug=True)
