from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, world"

if __name__ == "__main__":
    app.debug = True
    app.secret_key = "asdfghjkl"
    app.run('0.0.0.0',port=8000)
