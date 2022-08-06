from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    kwargs = {
        "name": 'Lisa',
        "song": 'LALISA'
    }
    return render_template(
        "index.html", **kwargs
    )
