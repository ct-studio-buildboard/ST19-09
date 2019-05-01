from flask import render_template, request, jsonify, redirect, url_for
from flask_cors import CORS, cross_origin

from app import app
from app.models import predict

# cors = CORS(app)
# app.config['CORS_HEADERS'] = "Content-Type"

@app.route('/')
def index():
    return render_template("login.html")

@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")

@app.route('/generate')
def generate():
    return render_template("generate.html")

@app.route('/complete')
def complete():
	return render_template("complete.html")

@app.route('/test')
def test_api():
	return render_template("test.html")

# @app.route('/test_inputs', methods=['POST'])
# def test_inputs():
#     keywords = request.get_json('keywords')['keywords']
#     print(keywords)
#     suggestion = predict.generate(keywords)
#     print(suggestion)
#     return redirect(url_for('result', keywords=keywords, suggestion=suggestion), code=307)

@app.route('/result', methods=['POST'])
def test_inputs():
    keywords = request.form['keyword']
    print(keywords)
    suggestion = predict.generate(keywords)
    print(suggestion)
    return render_template("result.html", keywords=keywords, suggestion=suggestion)

## Not working for some reason
# @app.route('/result', methods=['POST'])
# def suggest_result():
#     keywords = request.get_json('keywords')['keywords']
#     print(keywords)
#     suggestion = predict.generate(keywords)
#     return render_template("result.html", suggestion=suggestion, keywords=keywords)

# @app.route('/result', methods=['POST'])
# def result():
#     return render_template("result.html", suggestion=request.args.get("suggestion"), keywords=request.args.get("keywords"))