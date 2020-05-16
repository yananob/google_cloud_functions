import json

def load_conf():
    with open("conf.json", "r") as f:
        conf = json.load(f)
        return conf
