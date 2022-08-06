from flask import Flask, render_template, request
from pymongo import MongoClient
import datetime

app = Flask(__name__)
client = MongoClient(
    "mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false")
app.db = client.microblog
entries = []


@app.route('/examples')
def practice():
    kwargs = {
        "name": 'Lisa',
        "song": 'LALISA'
    }
    songs = [
        "New Rules",
        "Fever",
        "How You Like That"
    ]
    laptop_users = {
        "kai": "mac",
        "lisa": "windows",
        "linna": "chrome"
    }
    company = "Apple"
    return render_template(
        "index.html", **kwargs, songs=songs, company=company, laptop_users=laptop_users
    )


@app.route('/', methods=["GET", "POST"])
def home():
    # print([e for e in app.db.entires.find({})])
    if request.method == "POST":
        entry_content = request.form.get("content")
        formatted_date = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")
        entries.append((entry_content, formatted_date))
        app.db.entries.insert_one(
            {"content": entry_content, "date": formatted_date})
    entires_with_date = [
        (
            entry[0],
            entry[1],
            datetime.datetime.strptime(
                entry[1], "%Y-%m-%d %H:%M:%S").strftime("%b-%d %H:%M:%S")
        )
        for entry in entries
    ]
    return render_template("home.html", entries=entires_with_date)
