from requests import get as gt, post as pt


def post(params):
    response = pt("http://127.0.0.1:8000/api", data=params).json()
    return response


def get(params):
    response = gt("http://127.0.0.1:8000/api", params=params).json()
    print("////////////////////////////////////////")
    print(response)
    return response
