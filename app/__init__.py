from flask import Flask, render_template
from app.app import BASE_DIR, DATA_DIR
from models.Loader import DataLoader

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def hello_app():
        loader = DataLoader(DATA_DIR + '/stores.json')
        stores = loader.load_data()
        return render_template("index.html", stores=stores)

    return app
