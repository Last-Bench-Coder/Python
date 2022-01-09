import pyodbc
from flask import Flask
from flask_rebar import Rebar
from os import system
import itertools
import json

import database.connection_string as GetConnection

system('cls')

app = Flask(__name__)
rebar = Rebar()

v1_registery = rebar.create_handler_registry(prefix='/api/v1/')
v2_registery = rebar.create_handler_registry(prefix='/api/v2/')

connection = pyodbc.connect(GetConnection.connection)

@v1_registery.handles(rule='emp')
def emp_list():
    sql = "SELECT fullname,emailid,phone FROM EMPLOYEES"
    return list_employee(sql)

@v2_registery.handles(rule='emp')
def emp_list():
    sql = "SELECT * FROM EMPLOYEES"
    return list_employee(sql)


def list_employee(sql):
    data = {}
    cursor = connection.cursor()
    cursor.execute(sql)
    desc = cursor.description
    columns = [col[0] for col in desc]
    data = [dict(itertools.zip_longest(columns,i))for i in cursor.fetchall()]

    return json.dumps(data,sort_keys=True, default=str)

rebar.init_app(app)
if __name__=="__main__":
    app.run(port=9090,debug=True)