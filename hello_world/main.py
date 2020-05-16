from flask import Flask, request

app = Flask(__name__)


def hello_world(req):
    """Responds to any HTTP request.
    Args:
        req (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    request_json = req.get_json()
    if req.args and 'message' in req.args:
        return req.args.get('message')
    elif req.args and 'cat' in req.args:
        with open("test.txt", "r") as f:
            return "\n".join(f.readlines())
    elif request_json and 'message' in request_json:
        return request_json['message']
    else:
        return 'Hello World!'


@app.route("/")
def mock():
    return hello_world(request)


if __name__ == "__main__":
    app.run()
