from flask import Flask
from flask.logging import create_logger
import logging

app = Flask(__name__)
LOG = create_logger(app)
LOG.setLevel(logging.INFO)

@app.route("/")
def home():
    html = f"""<h3>LongNV43 DevOps Capstone Home</h3>
    <p>Update this page to include meaningful information</p>
    <p> Happy new year! </p>"""
    return html.format(format)

@app.route("/secret", methods=['GET'])
def secret():
    LOG.info(f"Someone accessed secret section")
    html = f"<h3>Do you know the way?</h3>"
    return html.format(format)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=False)
