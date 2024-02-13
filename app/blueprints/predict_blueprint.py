import logging

from flask import Blueprint, Response,make_response

predict_blueprint = Blueprint('predict_blueprint', __name__)

@predict_blueprint.route("/api/predict", methods=['GET'])
def predict():
    try:
        logging.info("Request Predict received")
        predicted_data = {"predicted": "banana"}
        return make_response(predicted_data, 200)
    except Exception as e:
        logging.error(f"Unknown error when handling predict. {e}")
        return Response(status=500)



