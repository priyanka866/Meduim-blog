from flask import Flask, request, jsonify

app = Flask(__name__)

def count_words(text):
    words = text.split()
    return len(words)

@app.route('/count_words', methods=['POST'])
def count_words_endpoint():
    try:
        data = request.get_json()

        # Check if 'Text' key is present in the JSON data
        if 'Text' not in data:
            return jsonify({'error': 'Text not found'}), 400

        user_text = data['Text']

        # Check if the input is empty
        if not user_text.strip():
            return jsonify({'error': 'Text cannot be empty or contain only whitespaces'}), 400

        # Call the function to count words
        result = count_words(user_text)

        return jsonify({'total_words': result})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)