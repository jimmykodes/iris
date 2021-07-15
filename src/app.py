import numpy as np
from flask import Flask, render_template, request, jsonify
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

app = Flask(__name__)

X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)


@app.route("/")
def index():
    return render_template("data.html", X_train=X_train, X_test=X_test, y_train=y_train)


@app.route("/test", methods=('POST',))
def test():
    guess = np.array(request.json)
    c = accuracy_score(y_test, guess, normalize=False)
    ac = accuracy_score(y_test, guess)
    return jsonify({"num_correct": int(c), "accuracy": ac})
