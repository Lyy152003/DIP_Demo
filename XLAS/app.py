# app.py

from flask import Flask, render_template, request, jsonify
from braille_converter import text_to_braille

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/user', methods=['GET', 'POST'])
def user():
    if request.method == 'POST':
        data = request.get_json()
        input_text = data.get('text', '')
        braille_result = text_to_braille(input_text)
        return jsonify({'braille_result': braille_result})
    return render_template('user.html')

if __name__ == '__main__':
    app.run(debug=True)
