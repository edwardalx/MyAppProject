from flask import Flask, request, jsonify

app = Flask(__name__)

# Storage
myDataName = []
myDataAge = []

@app.route('/collect-data', methods=['POST'])
def collect_data():
    data = request.json
    name = data.get('name')
    age = data.get('age')

    if name and age:
        myDataName.append(name)
        myDataAge.append(age)
        return jsonify({'status': 'success', 'message': f'Data saved: {name}, {age}'})
    else:
        return jsonify({'status': 'error', 'message': 'Invalid data'}), 400

# Retrieve Data Route
@app.route('/get-data', methods=['GET'])
def get_data():
    myData = dict(zip(myDataName, myDataAge))
    return jsonify(myData)

if __name__ == "__main__":
    app.run(debug=True)
