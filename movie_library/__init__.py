import os
from flask import Flask
from dotenv import load_dotenv
from pymongo import MongoClient

from movie_library.routes import pages

load_dotenv()


def create_app():
    app = Flask(__name__)
    client=MongoClient(os.getenv("MONGODB_URI"))
    app.db=client.FlaskBlog


    app.config["SECRET_KEY"] = os.environ.get(
        "SECRET_KEY")
   
    app.register_blueprint(pages)
    return app