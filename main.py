from flask import Flask, jsonify, render_template_string
import os

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
