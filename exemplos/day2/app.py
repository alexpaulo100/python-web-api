from flask import Flask

app = Flask(__name__)

app.config["APP_NAME"] = "Meu Blog"


@app.errorhandler(404)
def not_found_page(error):
    return f"Not Found on {app.config['APP_NAME']}"



@app.route("/")
def hello():
    return "<strong>Hello World</strong>"


