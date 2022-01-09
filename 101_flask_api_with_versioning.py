from flask import Flask, app
from flask_rebar import Rebar
import json

data = [
    {"empId": 100, "fullname": "Chakrapani U", "emailId": "chakrapani@test.com"},
    {"empId": 101, "fullname": "shraddha u", "emailId": "shraddha@test.com"},
    {"empId": 102, "fullname": "shreshta u", "emailId": "shreshta@test.com"}
]

data2 = [
    {"empId": 100, "fullname": "Chakrapani U", "emailId": "chakrapani@test.com","Phone":9888556622},
    {"empId": 101, "fullname": "shraddha u", "emailId": "shraddha@test.com","Phone":9988116622},
    {"empId": 102, "fullname": "shreshta u", "emailId": "shreshta@test.com","Phone":99880056622}
]

rebar =Rebar()
v1=rebar.create_handler_registry(prefix='/api/v1')
v2=rebar.create_handler_registry(prefix='/api/v2')

@v1.handles(rule="/emp")
def employee():
    return json.dumps(data)

@v2.handles(rule="/emp")
def employee():
    return json.dumps(data2)

app=Flask(__name__)
rebar.init_app(app)

if __name__ == "__main__":
    app.run(port=9090)
