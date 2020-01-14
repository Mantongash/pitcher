from pitcher.models import User, Pitch
from pitcher import app, bcrypt, db
from flask import render_template, redirect, flash,url_for
from pitcher.forms import RegistrationForm, LoginForm
@app.route("/")
@app.route("/home")
def home():
    posts = [
        {
            "title": "The Genius",
            "author": "Michaelangelo",
            "pitch": "Genius is eternal patience. I saw the angel in the marble and carved until I set him free. Trifles make perfection, and perfection is no trifle.",
            "date": "2nd Jan, 2019"
        },
        {
            "title": "The Inspiration",
            "author": "Albert Einstein",
            "pitch": "Insanity: doing the same thing over and over again and expecting different results. Imagination is more important than knowledge. Imagination is everything. It is the preview of life's coming attractions.",
            "date": "5th Dec, 2000"
        },
        {
            "title": "Be Yourself",
            "author": "Anonymous",
            "pitch": "Be who you are and say what you feel, because those who mind don't matter and those who matter don't mind",
            "date": "12th Aug, 1993"
        }
    ]

    return render_template("home.html", title="Home", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/login", methods=["POST", "GET"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@gmail.com" and form.password.data == "123":
            flash("You are successfully logged in !", "success")
        else:
            flash("Please check your email and password", "danger")

        return redirect(url_for("home"))
    return render_template("login.html", title="Log In", form=form)


@app.route("/signup", methods=["POST", "GET"])
def signup():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password=bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash("Your Account has been created. You can now log in.", "success")
        return redirect(url_for("login"))
    return render_template("signup.html", title="Sign Up", form=form)
