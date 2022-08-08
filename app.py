from venv import create
from flask import Flask, render_template, request
from pymongo import MongoClient
import datetime


def create_app():
    app = Flask(__name__)
    return app
