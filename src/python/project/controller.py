from flask import Flask
from flask import request
from flask import jsonify
import cv2
import numpy as np
import classifyInteger
import subprocess
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/recognize/score", methods=['POST'])
def recognize_score():
    inputFile = request.files['score_image']
    np_array = np.fromstring(inputFile.stream.getvalue(), np.uint8)
    cv_img = cv2.imdecode(np_array, cv2.CV_LOAD_IMAGE_COLOR)
    cv2.imwrite(inputFile.filename, cv_img)
    score = classifyInteger.get_integer(inputFile.filename)
    subprocess.call('rm ' + inputFile.filename, shell=True)
    return jsonify(score=score)

if __name__ == "__main__":
    app.run()
