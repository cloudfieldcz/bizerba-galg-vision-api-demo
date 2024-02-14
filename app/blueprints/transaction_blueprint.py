import logging
from datetime import datetime

from flask import Blueprint, make_response, request, jsonify

transaction_blueprint = Blueprint('transaction_blueprint', __name__)


@transaction_blueprint.route("/api/transaction_add", methods=['GET', 'POST'])
def transaction_add():
    try:
        logging.info("Handling method transaction_add")
        message = {"state": "transaction data accepted"}
        return make_response(message, 200)

    except Exception as e:
        logging.error(f"Unknown error when handling transaction_add function {e}")


@transaction_blueprint.route("/api/transaction_post", methods=['GET', 'POST'])
def transaction_post():
    try:
        logging.info("Handling method transaction_post")
        json_data = request.json

        required_parameters = ['sell_id', 'device_id', 'time', 'neural_version', 'success', 'sold_assortment', 'success_position','position_1_percent', 'position_2_percent', 'position_3_percent', 'position_4_percent', 'position_5_percent', 'position_1_assortment', 'position_2_assortment', 'position_3_assortment', 'position_4_assortment', 'position_5_assortment', 'duration']
        decimal_parameters = ['position_1_percent', 'position_2_percent', 'position_3_percent', 'position_4_percent', 'position_5_percent']

        # Check if all required parameters are present
        missing_parameters = [param for param in required_parameters if param not in json_data]
        if missing_parameters:
            error_message = {"error": f"Parameters {missing_parameters} are missing in the request."}
            return jsonify(error_message), 400

        # Perform additional validation for 'time' parameter format
        if not validate_time_format(json_data['time']):
            error_message = {"error": "Invalid format for 'time' parameter. Expected format: yyyyMMddhhmm."}
            return jsonify(error_message), 400

        # Perform additional validation for 'success' parameter boolean value
        success_value = json_data.get('success')
        if not isinstance(success_value, bool):
            error_message = {"error": "Invalid value for 'success' parameter. Expected a boolean (True/False)."}
            return jsonify(error_message), 400

        # Perform additional validation for 'success_position' parameter value
        success_position_value = json_data.get('success_position')
        valid_success_positions = [-1, 0, 1, 2, 3, 4, 5, 6, 7]
        if success_position_value not in valid_success_positions:
            error_message = {
                "error": "Invalid value for 'success_position' parameter. Expected one of -1, 0, 1, 2, 3, 4, 5, 6, 7."}
            return jsonify(error_message), 400

        # Check decimal parameters with maximum of 2 decimal points
        for param in decimal_parameters:
            if param not in json_data:
                error_message = {"error": f"Parameter '{param}' is missing in the request."}
                return jsonify(error_message), 400

            position_percent_value = json_data.get(param)
            if not validate_decimal_value(position_percent_value):
                error_message = {
                    "error": f"Invalid value for '{param}' parameter. Expected a decimal value from 0 to 100 with 2 decimal places."}
                return jsonify(error_message), 400

        # If all validations pass, process the transaction
        # Return success response
        return jsonify({"message": "Transaction processed successfully."}), 200

    except Exception as e:
        logging.error(f"Error in transaction_post: {str(e)}")
        error_message = {"error": "An unexpected error occurred during transaction processing.  E:"+str(e)}
        return jsonify(error_message), 500


def validate_time_format(time_str):
    try:
        datetime.strptime(time_str, '%Y%m%d%H%M')
        return True
    except ValueError:
        return False


def validate_decimal_value(value):
    try:
        decimal_value = float(value)
        if decimal_value < 0 or decimal_value > 100:
            return False

        # Check if the number has at most 2 decimal places
        if decimal_value != int(decimal_value):
            decimal_places = len(str(decimal_value).split('.')[-1])
            if decimal_places > 2:
                return False

        return True

    except (ValueError, TypeError):
        return False
