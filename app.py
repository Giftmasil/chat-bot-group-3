from flask import Flask, request, jsonify
from flask_cors import CORS
from first_aid_bot import FirstAidBot

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

bot = FirstAidBot()

@app.route('/get_advice', methods=['POST'])
def get_advice():
    data = request.get_json()
    user_input = data.get('query')
    if not user_input:
        return jsonify({'response': 'Please enter a description of the emergency or condition.'}), 400
    response = bot.get_first_aid_advice(user_input)
    # Ensure the response is properly formatted
    response = response.strip()  # Remove any leading/trailing whitespace
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True, port=5001)  # Change port if needed
