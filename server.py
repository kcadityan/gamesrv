from flask import Flask, jsonify, request

app = Flask(__name__)

# Define the API endpoint
@app.route('/hit', methods=['POST'])
def hit():
    # Get the JSON data from the request
    data = request.json
    print(jsonify(data))
    # Implement your logic here based on the received data
    # For demonstration purposes, just return a JSON response echoing the received data
    return jsonify(data)

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)  # Run the server in debug mode for development
