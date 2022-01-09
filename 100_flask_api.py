from flask import Flask
from os import system
import json

app = Flask(__name__)

data = [
    {"empId": 100, "fullname": "Chakrapani U", "emailId": "chakrapani@test.com"},
    {"empId": 101, "fullname": "shraddha u", "emailId": "shraddha@test.com"},
    {"empId": 102, "fullname": "shreshta u", "emailId": "shreshta@test.com"}
]


@app.route("/api/v1/employees", methods=["GET"])
def welcome():
    return json.dumps(data)


if __name__ == "__main__":
    app.run(port=9090)
