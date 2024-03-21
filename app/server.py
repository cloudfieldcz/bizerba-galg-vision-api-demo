import logging
import os

from flask import Flask, send_from_directory
from flasgger import Swagger

from waitress import serve

from app import configuration
from app.blueprints.predict_blueprint import predict_blueprint
from app.blueprints.transaction_blueprint import transaction_blueprint


def flask_app():
    app = Flask(__name__)
    app.secret_key = os.urandom(32)

    @app.route("/")
    def client():
        return send_from_directory('client/public', 'index.html')

    app.register_blueprint(predict_blueprint)
    app.register_blueprint(transaction_blueprint)

    return app


def server(host: str = None, port: int = None):
    manager_app = flask_app()
    configuration.configure(manager_app)
    logging.info(f"Starting server on http://{host}:{port}")
    swagger = Swagger(manager_app)
    serve(manager_app, port=port, threads=5)
