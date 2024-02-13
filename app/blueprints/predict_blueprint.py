import logging

from flask import Blueprint, Response,make_response

predict_blueprint = Blueprint('predict_blueprint', __name__)

@predict_blueprint.route("/api/predict", methods=['GET'])
def predict():
    try:
        logging.info("Request Predict received")


        predicted_data = {
            "items": [
                {"label": "onion", "matchRate": 37},
                {"label": "apple_red", "matchRate": 19},
                {"label": "apple_jonagold", "matchRate": 13},
                {"label": "litchee", "matchRate": 6},
                {"label": "nectarine", "matchRate": 3},
                {"label": "apple_red_jonaprince", "matchRate": 3},
                {"label": "potato_red", "matchRate": 3},
                {"label": "tangerines", "matchRate": 3}
            ],
            "best_suggestion":
                {"label": "onion", "matchRate": 37},
            "duration": 0.15556540000034147
        }
        return make_response(predicted_data, 200)
    except Exception as e:
        logging.error(f"Unknown error when handling predict. {e}")
        return Response(status=500)



