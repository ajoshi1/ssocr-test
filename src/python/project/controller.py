from flask import Flask
from flask import request
from flask import jsonify
import classifyInteger

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/recognize/score", methods=['POST'])
def recognize_score():
    inputFile = request.files['score_image']
    score = classifyInteger.get_integer(inputFile.stream.getvalue())
    return jsonify(score=score)

if __name__ == "__main__":
    app.run()
