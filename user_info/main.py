from flask import Flask, request, Response
import csv
import json
import pandas

app = Flask(__name__)


def user_info(req):
    """Responds to any HTTP request.
    Args:
        req (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """

    df = pandas.read_csv("./user_list.csv", index_col="USER_ID")

    print(req.args)
    if not req.args or 'user' not in req.args:
        return "user parameter needed."
    user_id = req.args["user"]

    row = df.loc[user_id]

    message = {
        "user_id": user_id,
        "cluster": row["CLUSTER"],
        "version": row["VER."],
        "item_count": str(row["ITEM"]),
        "badges": [badge.replace("[", "").replace("]", "") for badge in row["BADGES"].split("][")],
    }
    resp = Response(json.dumps(message, ensure_ascii=False))
    resp.headers["content-type"] = "application/json"
    return resp


@app.route("/")
def mock():
    return user_info(request)


if __name__ == "__main__":
    app.run()
