from flask import Flask, request, jsonify

app = Flask(__name__)

# Initialize storage
myDataName = []
myDataAge = []

@app.route('/collect-data', methods=['POST'])
def collect_data():
    data = request.json  # Parse JSON data from the frontend
    name = data.get('name')
    age = data.get('age')

    if name and name.lower() != "exit":
        myDataName.append(name)
        try:
            age = int(age)
            myDataAge.append(age)
        except ValueError:
            return jsonify({"error": "Invalid age provided"}), 400
        
        # Create dictionary of collected data
        myData = dict(zip(myDataName, myDataAge))
        return jsonify({"message": f"Data added: {name}, {age}", "data": myData}), 200
    
    return jsonify({"message": "Exit received, stopping input.", "data": dict(zip(myDataName, myDataAge))}), 200

if __name__ == '__main__':
    app.run(debug=True)
