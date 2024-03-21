import logging

from flask import Blueprint, Response, make_response, request, jsonify

predict_blueprint = Blueprint('predict_blueprint', __name__)

ALLOWED_GROUP_PARAMS = ['fruit', 'vegetable', 'bakery']


@predict_blueprint.route("/api/predict", methods=['GET', 'POST'])
def predict():
    """
     Get user details by ID
     ---
     parameters:
       - name: user_id
         in: path
         type: integer
         required: true
         description: User ID
     responses:
       200:
         description: User details retrieved successfully
     """

    try:
        logging.info("Request Predict received")

        for header, value in request.headers.items():
            logging.info(f"Received header: {header}: {value}")

        # if group_param not in ALLOWED_GROUP_PARAMS:
        #    return make_response({"error": "Invalid group_param. Allowed values: 'fruit', 'vegetable', 'bakery'"}, 400)

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
