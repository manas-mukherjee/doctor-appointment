from flask import Flask, request, jsonify
import flask
import json
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

# map as database 
countries = [
    {"id": 1, "name": "Thailand", "capital": "Bangkok", "area": 513120},
    {"id": 2, "name": "Australia", "capital": "Canberra", "area": 7617930},
    {"id": 3, "name": "Egypt", "capital": "Cairo", "area": 1010408},
]

# Get all appointments
@app.get("/appointment")
def get_countries():
    print("get countries called: {}".format(countries))
    return jsonify(countries)

# Get all appointments
@app.get("/appointment/{id}")
def get_appointment_by_id(id):
    print("get countries called: {}".format(countries))

    for country in countries:
        if country["id"] == id:
            return jsonify(country)
    return jsonify({"error": "Country not found"})
    
    return jsonify(countries)

# Generate an unique appointment id
def _find_next_id():
    return max(country["id"] for country in countries) + 1

# Create a new appointment
@app.route('/appointment', methods=["POST"])
def add_country():
    if request.is_json:
        country = request.get_json()
        country["id"] = _find_next_id()
        countries.append(country)
        print("countries: {}".format(countries))
        return country, 201
    return {"error": "Request must be JSON"}, 415

if __name__ == "__main__":
    port_number = 6969
    # Start the server on the port specified above
    app.run("localhost", port_number)