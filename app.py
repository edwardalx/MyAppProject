from flask import Flask, request, jsonify

app = Flask(__name__)

# Initialize storage (In-memory storage for demonstration purposes)
myDataName = []
myDataAge = []

# Route to collect data (Data Entry)
@app.route('/collect-data', methods=['POST'])
def collect_data():
    # Parse JSON data sent from the frontend
    data = request.json
    name = data.get('name')
    age = data.get('age')

    # Validate input
    if not name or not age:
        return jsonify({'status': 'error', 'message': 'Name and age are required!'}), 400

    try:
        # Convert age to an integer (if not already)
        age = int(age)
    except ValueError:
        return jsonify({'status': 'error', 'message': 'Age must be a number!'}), 400

    # Store the data
    myDataName.append(name)
    myDataAge.append(age)

    return jsonify({'status': 'success', 'message': f'Data saved: Name={name}, Age={age}'})

# Route to retrieve data (Data Retrieval)
@app.route('/get-data', methods=['GET'])
def get_data():
    # Combine names and ages into a dictionary
    myData = dict(zip(myDataName, myDataAge))

    # Return the data as JSON
    return jsonify({'status': 'success', 'data': myData})

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
