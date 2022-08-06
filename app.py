from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    kwargs = {
        "name": 'Lisa',
        "song": 'LALISA'
    }
    songs = [
        "New Rules",
        "Fever",
        "How You Like That"
    ]
    company = "Apple"
    return render_template(
        "index.html", **kwargs, songs=songs, company=company
    )
