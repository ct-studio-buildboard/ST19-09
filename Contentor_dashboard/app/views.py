from flask import render_template, request, jsonify

from app import app
from app.models import test, food

@app.route('/')
def index():
    return render_template("login.html")

@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")

@app.route('/generate')
def generate():
    return render_template("generate.html")

@app.route('/result')
def result():
    return render_template("result.html")

@app.route('/complete')
def complete():
	return render_template("complete.html")

@app.route('/test')
def test_api():
	return render_template("test.html")

@app.route('/test_inputs', methods=['POST'])
def test_inputs():
    items = request.get_json('items')['items']
    return jsonify({'status': 'OK', 'text': 'It works', 'items': items})

@app.route('/test_user', methods=['POST'])
def signUpUser():
    user =  request.form['my_name']
    return jsonify({'status':'OK', 'user':user, 'test':test.check_test(), 'food': food.check_food()});