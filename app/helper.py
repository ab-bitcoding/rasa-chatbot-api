import uuid
import json


def format_response(
    detail_type=None, data=None, loc=None, msg=None, input_value=None, reason=None
):
    response_detail = {}
    if detail_type is not None:
        response_detail["type"] = detail_type
    if data is not None:
        response_detail["data"] = data
    if loc is not None:
        response_detail["loc"] = [loc]
    if msg is not None:
        response_detail["msg"] = msg
    if input_value is not None:
        response_detail["input"] = input_value
    if reason is not None:
        response_detail["ctx"] = {"reason": reason}
    response_detail["traceback_id"] = str(uuid.uuid4())

    formatted_response = {"detail": [response_detail]}
    return formatted_response

def exception_format_response(
    detail_type=None, data=None, loc=None, msg=None, input_value=None, reason=None   
):
    response_detail = {}
    if detail_type is not None:
        response_detail["type"] = detail_type
    if data is not None:
        response_detail["data"] = data
    if loc is not None:
        response_detail["loc"] = [loc]
    if msg is not None:
        response_detail["msg"] = msg
    if input_value is not None:
        response_detail["input"] = input_value
    if reason is not None:
        response_detail["ctx"] = {"reason": reason}
    response_detail["traceback_id"] = str(uuid.uuid4())


    formatted_response = {"detail": [response_detail]}
    return formatted_response


def load_error_details(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)