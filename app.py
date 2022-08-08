from flask import Flask, render_template, request
from pymongo import MongoClient


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return render_template('index.html')
