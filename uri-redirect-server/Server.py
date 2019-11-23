from flask import Flask

import os

app = Flask(__name__)

@app.route("/callback")
def callback():
    return "OK"

if __name__ == "__main__":
    app.run(host="localhost", port=int(os.environ.get("PORT", 8888)))
