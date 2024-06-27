from flask import Flask, request
from my_openai import call_openAI

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/signin")
def sign_in():
    return "<p>Sign in Page</p>"


@app.route("/place", methods=["POST"])
def json_example():
    request_data = request.get_json()

    name = request_data["name"]
    desc = request_data["description"]

    response = call_openAI(desc)
    return """
           The name value is: {}
           The desc value is: {}
           The generated response is: {}""".format(
        name, desc, response
    )
