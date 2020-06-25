import os
import debugpy
from flask import Flask


debugpy.listen(("0.0.0.0", 5678))
debugpy.wait_for_client()

app = Flask(__name__)

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    message = "Hello World"
    return message

if __name__ == "__main__":
    app.run(host="0.0.0.0")