from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route(rule = "/api", methods = ["GET", "POST", "PUT"])
def handle_request():
    if request.method == "GET":
        return "This is the Get endpoint"
    if request.method == "POST":
        payload = request.get_json()
        cap_text = payload['text'].upper()
        res = {'cap text' : cap_text}
        print(res)
        return jsonify(res)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)