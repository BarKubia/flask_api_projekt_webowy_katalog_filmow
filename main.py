from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    movies = []
    for n in range (0,8):
        movies.append(n)
    
    return render_template("homepage.html", movies=movies)

