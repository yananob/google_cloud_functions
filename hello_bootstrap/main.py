from flask import Flask, request, render_template

app = Flask(__name__)


def bootstrap(req):
    """Responds to any HTTP request.
    Args:
        req (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """

    result = ""
    if req.args and "target" in req.args:
        result = req.args["message"]

    return render_template("form.html", result=result)


@app.route("/")
@app.route("/bootstrap")
def mock():
    return bootstrap(request)


if __name__ == "__main__":
    app.run()
