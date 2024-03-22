import logging
from datetime import datetime

from flask import Blueprint, make_response, request, jsonify

transaction_blueprint = Blueprint('transaction_blueprint', __name__)


@transaction_blueprint.route("/api/v1/transaction", methods=['POST'])
def add_transaction():
    """
       Process transaction data
       ---
       tags:
         - Transaction
       parameters:
         - in: body
           name: json_data
           description: transaction data
           required: true
           schema:
             type: object
             properties:
               sell_id:
                 description: "Unique ID for the sell, provided by Tangram"
                 type: string
               device_id:
                 description: "Unique ID for the machine"
                 type: string
               suggestion_id:
                 description: "Identication of previouse suggestion method invocation, to pair suggestion and sell data."
                 type: string
               time:
                 description: "Time of transaction being"
                 type: datetime
               sold_assortment:
                 description: "Final PLU selected by cashier"
                 type: string
               duration:
                 description: "Total amount of time, in miliseconds, for whole process."
                 type: float
       responses:
         200:
           description: Data processed successfully
         400:
           description: Occurs when some required attribute is missing. All attributes are required.
       """

    try:
        logging.info("Handling method transaction_post")
        json_data = request.json

        required_parameters = ['sell_id', 'device_id', 'suggestion_id', 'time', 'sold_assortment', 'duration']

        # Check if all required parameters are present
        missing_parameters = [param for param in required_parameters if param not in json_data]
        if missing_parameters:
            error_message = {"error": f"Parameters {missing_parameters} are missing in the request."}
            return jsonify(error_message), 400

        # Validate and parse the 'time' parameter in ISO format
        if 'time' in json_data:
            try:
                json_data['time'] = datetime.strptime(json_data['time'], '%Y%m%d%H%M').isoformat()
            except ValueError:
                error_message = {"error": "Invalid format for 'time' parameter. Expected format: yyyymmddhhmm."}
                return jsonify(error_message), 400

        # If all validations pass, process the transaction
        # Return success response
        return jsonify({"message": "Transaction processed successfully."}), 200

    except Exception as e:
        logging.error(f"Error in transaction_post: {str(e)}")
        error_message = {"error": "An unexpected error occurred during transaction processing.  E:" + str(e)}
        return jsonify(error_message), 500


def validate_time_format(time_str):
    try:
        datetime.strptime(time_str, '%Y%m%d%H%M')
        return True
    except ValueError:
        return False
