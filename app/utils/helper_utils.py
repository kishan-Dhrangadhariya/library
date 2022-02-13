from flask import Response, request
from decorator import decorator
import json


def parameter_extractor(params):
    def wrapper(f, *args, **kwargs):
        json_object = {}
        if request.method.lower() == "get":
            json_object.update(request.args)
        elif request.method.lower() in ["post", "put"]:
            json_object.update(request.json)
        elif request.content_type and "multipart/form-data" in request.content_type:
            if getattr(request, "files"):
                json_object.update(request.files)
            if getattr(request, "data"):
                json_object.update(request.data.to_dict())
        else:
            # todo add other request type as per need
            pass
        kwargs.update(json_object)
        return f(*args, **kwargs)
    return decorator(wrapper)


def response_dict(data=None, status=200, message=None):
    """
    Returns a response object for DB searches
    """
    resp_dict = {}
    if status == 200:
        if data is not None:
            resp_dict["data"] = data
        if message is not None:
            resp_dict["message"] = message
        resp_dict["success"] = True

    else:
        resp_dict["error"] = message
        resp_dict["success"] = False

    return Response(
        response=json.dumps(resp_dict),
        status=status,
        mimetype="application/json",
    )
