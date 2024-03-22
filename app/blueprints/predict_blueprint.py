import logging
import os
import tempfile
import time

from flask import Blueprint, Response, make_response, request, jsonify

predict_blueprint = Blueprint('predict_blueprint', __name__)

ALLOWED_GROUP_PARAMS = ['fruit', 'vegetable', 'bakery']


@predict_blueprint.route("/api/v1/suggest/<group>", methods=['POST'])
def predict(group):
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
          description: "Image file to process/suggest"
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
                          description: "humanreadable assortment name"
                        plu:
                          type: "string"
                          description: "assortment code"
                        matchrate:
                          type: "float"
                          description: "percentage of assortment matches"
                  best_suggestion:
                    type: "object"
                    description: "redicted item with highest score"
                    properties:
                      label:
                        type: "string"
                        description: "humanreadable assortment name"
                      plu:
                        type: "string"
                        description: "assortment code"
                      matchrate:
                        type: "float"
                        description: "percentage of assortment matches"
                  duration:
                    type: "float"
                    description: "duration of suggestion process"
                  suggestion_id:
                    description: "unique id of suggestion, will be used for transaction update"
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

        data = request.get_data()
        logging.info(f"Input data size: {len(data)} bytes.")
        tmp_file = tempfile.NamedTemporaryFile(delete=False)
        try:
            tmp_file.write(data)
            dump_input_image(data)
        except Exception as e:
            print(e)

        if group not in ALLOWED_GROUP_PARAMS:
           return make_response({"error": f"Invalid group. Received {group}. Allowed values: 'fruit', 'vegetable', 'bakery'"}, 404)

        predicted_data = {
            "items": [
                {"label": "onion", "plu": "101", "matchRate": 37},
                {"label": "apple_red", "plu": "102", "matchRate": 19},
                {"label": "apple_jonagold", "plu": "103",  "matchRate": 13},
                {"label": "litchee", "plu": "104",  "matchRate": 6},
                {"label": "nectarine", "plu": "105",  "matchRate": 3},
                {"label": "apple_red_jonaprince", "plu": "119",  "matchRate": 3},
                {"label": "potato_red", "plu": "m1010",  "matchRate": 3},
                {"label": "tangerines", "plu": "10200",  "matchRate": 3}
            ],
            "best_suggestion":
                {"label": "onion", "plu": "101",  "matchRate": 37},
            "duration": 0.15556540000034147,
            "suggestion_id": "abc-1234"
        }
        return make_response(predicted_data, 200)
    except Exception as e:
        logging.error(f"Unknown error when handling predict. {e}")
        return Response(status=500)

def dump_input_image(data):
    image_path = os.path.join("last_image.png")
    with (open(image_path, "wb")) as f:
        f.write(data)

