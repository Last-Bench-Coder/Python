from flask import Flask
from flask_rebar import Rebar
import json

v1_data = json.load(open('data/employee_v1.json','r'))
v2_data = json.load(open('data/employee_v2.json','r'))

app = Flask(__name__)
rebar = Rebar()
v1_registery = rebar.create_handler_registry(prefix='/api/v1')
v2_registery = rebar.create_handler_registry(prefix='/api/v2')

@v1_registery.handles(rule='/emp')
def employee():
    return json.dumps(v1_data)

@v2_registery.handles(rule='/emp')
def employee():
    return json.dumps(v2_data)

rebar.init_app(app)

if __name__ == '__main__':
    app.run(port="9090")

