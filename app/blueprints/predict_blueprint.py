import logging

from flask import Blueprint, Response, make_response, request, jsonify

predict_blueprint = Blueprint('predict_blueprint', __name__)

ALLOWED_GROUP_PARAMS = ['fruit', 'vegetable', 'bakery']


@predict_blueprint.route("/api/v1/suggest/{group}", methods=['POST'])
def predict():
    """
     Predict assortment from the input image
     ---
      tags:
         - Object recognition
      parameters:
        - in: path
          name: group
          type: string
          required: true
          description: "Group for which suggestions are requested."
        - in: formData
          name: image
          type: file
          required: true
          description: "Image file to process"
      responses:
        200:
          description: "Successful operation"
          schema:
            type: "object"
            properties:
              predicted_data:
                type: "object"
                properties:
                  items:
                    type: "array"
                    items:
                      type: "object"
                      properties:
                        label:
                          type: "string"
                        plu:
                          type: "string"
                        matchrate:
                          type: "number"
                  best_suggestion:
                    type: "object"
                    properties:
                      label:
                        type: "string"
                      plu:
                        type: "string"
                      matchrate:
                        type: "number"
                  duration:
                    type: "number"
                  suggestion_id:
                    type: "string"
        404:
          description: "Bad request - wrong group name or empty image"
      consumes:
        - "multipart/form-data"
     """

    try:
        logging.info("Request Predict received")

        for header, value in request.headers.items():
            logging.info(f"Received header: {header}: {value}")

        request_data = request.get_json()

        group_param = request_data["group"]
        if group_param not in ALLOWED_GROUP_PARAMS:
           return make_response({"error": "Invalid group_param. Allowed values: 'fruit', 'vegetable', 'bakery'"}, 404)

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
            "duration": 0.15556540000034147,
            "suggestion_id": "abc-1234"
        }
        return make_response(predicted_data, 200)
    except Exception as e:
        logging.error(f"Unknown error when handling predict. {e}")
        return Response(status=500)
