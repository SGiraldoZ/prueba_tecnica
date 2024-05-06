from flask import Flask
from fibonacci.fibonacci_bp import Fibonacci_bp

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Page under construction</p>"


app.register_blueprint(Fibonacci_bp, url_prefix="/fibonacci_hora")


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)