import logging
import urllib.request, urllib.parse
from flask import Flask, request, render_template
from common.utils import load_conf

app = Flask(__name__)

URL = 'https://autoremotejoaomgcd.appspot.com/sendmessage'

LOG_LEVEL = logging.INFO

# ?key=
# &message=jp_women%20%E3%83%86%E3%82%B9%E3%83%88=:=voice


def send_request(conf, speaker, message):

    message = message.replace(" ", ",")

    data = {
        "key": conf["token"],
        "message": "{} {}=:=voice".format(speaker, message),
    }
    
    logging.info("speaker: {}, message: {}".format(speaker, message))
    req = urllib.request.Request("{}?{}".format(URL, urllib.parse.urlencode(data)))
    # res = urllib.request.urlopen(req)
    # logging.info("response: {}".format(res.read()))
    with urllib.request.urlopen(req) as res:
        logging.info("response: {}".format(res.read()))


def n5_voice(req):
    """Responds to any HTTP request.
    Args:
        req (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """

    conf = load_conf()

    logging.basicConfig(format="[%(asctime)s] [%(levelname)s] %(message)s",
                        level=LOG_LEVEL, datefmt="%Y/%m/%d %H:%M:%S")
    logging.info("args: {}".format(req.args))

    feedback = ""
    speaker = req.args.get("speaker", "")
    message = req.args.get("message", "")
    if speaker and message:
        send_request(conf, speaker, message)
        feedback = "Message successfully sent."

    return render_template("form.html", feedback=feedback)


@app.route("/")
@app.route("/n5_voice")
def mock():
    return n5_voice(request)


if __name__ == "__main__":
    LOG_LEVEL = logging.DEBUG
    app.run()
