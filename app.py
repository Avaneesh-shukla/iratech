#first pip install flask
from flask import Flask, request

app = Flask(__name__)

@app.route("/api/v1/calculate", methods=['POST'])
def get_bot_response():
    form_data = request.get_json(force=True)
    x = form_data["x"]
    n = form_data["n"]
    s=0
    for i in range(1,n+1):
        s+=(1/(x**i))
    return str(s)


if __name__ == "__main__":
    app.run()
