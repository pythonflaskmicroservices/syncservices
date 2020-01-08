from flask import Flask, jsonify, request
import requests
app = Flask(__name__)

@app.route('/numbertototal/<int:num>')
def numbertototal(num):
    response = requests.get('http://localhost:4000/totalling/'+str(num))
    return response.text
app.run()
