from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


def caesar_cipher(text, shift, mode):
    result = ""

    if mode == "decrypt":
        shift = -shift

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char

    return result


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/encrypt', methods=['POST'])
def encrypt():
    try:
        data = request.json
        message = data.get('message', '')
        shift = int(data.get('shift', 0))
        output = caesar_cipher(message, shift, 'encrypt')
        return jsonify({'success': True, 'output': output})
    except ValueError:
        return jsonify({'success': False, 'error': 'Shift value must be an integer'})


@app.route('/decrypt', methods=['POST'])
def decrypt():
    try:
        data = request.json
        message = data.get('message', '')
        shift = int(data.get('shift', 0))
        output = caesar_cipher(message, shift, 'decrypt')
        return jsonify({'success': True, 'output': output})
    except ValueError:
        return jsonify({'success': False, 'error': 'Shift value must be an integer'})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
