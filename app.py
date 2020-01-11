from flask import Flask, render_template

app = Flask(__name__)


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
        "title":"Be Yourself",
        "author": "Anonymous",
        "pitch": "Be who you are and say what you feel, because those who mind don't matter and those who matter don't mind",
        "date": "12th Aug, 1993"
    }

]
@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", title="The Pitcher", posts=posts)


if __name__ == "__main__":
    app.run(debug=True)
