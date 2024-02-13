import logging

from flask import Blueprint,  make_response

transaction_blueprint = Blueprint('transaction_blueprint', __name__)


@transaction_blueprint.route("/api/transaction_add", methods=['GET'])
def transaction_add():
    try:
        logging.info("Handling method transaction_add")
        message = {"state": "transaction data accepted"}
        return make_response(message, 200)

    except Exception as e:
        logging.error(f"Unknown error when handling transaction_add function {e}")
