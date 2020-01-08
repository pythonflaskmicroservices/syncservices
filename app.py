from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/totalling/<int:number>')
def totalling(number):
    numbers = range(number)
    total = sum(numbers)
    return jsonify({'total':total})

app.run(port=4000)

