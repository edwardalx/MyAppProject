from flask import Flask, request, jsonify

app = Flask(__name__)

# Initialize storage (In-memory)
myDataName = []
myDataAge = []

# Data Entry Route
@app.route('/collect-data', methods=['POST'])
def collect_data():
    data = request.json
    name = data.get('name')
    age = data.get('age')

    if not name or not age:
        return jsonify({'status': 'error', 'message': 'Name and age are required!'}), 400

    try:
        age = int(age)
    except ValueError:
        return jsonify({'status': 'error', 'message': 'Age must be a number!'}), 400

    myDataName.append(name)
    myDataAge.append(age)
    return jsonify({'status': 'success', 'message': f'Data saved: Name={name}, Age={age}'})

# Data Retrieval Route
@app.route('/get-data', methods=['GET'])
def get_data():
    myData = dict(zip(myDataName, myDataAge))
    return jsonify({'status': 'success', 'data': myData})

if __name__ == "__main__":
    app.run(debug=True)
