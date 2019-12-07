#!/usr/bin/python3
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps

import mysql.connector

conn = mysql.connector.connect(user='root', password='mrHDEZ93.',
                              host='127.0.0.1',
                              database='OurWay')

db_connect = create_engine('sqlite:///chinook.db')
app = Flask(__name__)
api = Api(app)


class Rutas(Resource):
    def get(self):
        conn = mysql.connector.connect(user='root', password='mrHDEZ93.', host='127.0.0.1', database='OurWay')
        cursor = conn.cursor()
        cursor.execute("select * from Rutas;")
        rutas = []
        for (ID, URL, NOMBRE) in cursor:
            rutas.append({"id": ID, "url": URL, "nombre": NOMBRE})
        conn.close()
        return str(rutas)
    
    
class Ubicaciones(Resource):
    def get(self):
        conn = mysql.connector.connect(user='root', password='mrHDEZ93.', host='127.0.0.1', database='OurWay')
        cursor = conn.cursor()
        cursor.execute("select * from Ubicaciones, Ruta_Ubicaciones where ID_UBICACIONES = Ubicaciones.ID;")
        rutas = []
        for (LATITUDE, LONGITUDE, TIMESTAMP) in cursor:
            rutas.append({"lat": LATITUDE, "lng": LONGITUDE, "timestamp": TIMESTAMP})
        conn.close()
        return str(rutas)
    

    
class Employees_Name(Resource):
    def get(self, employee_id):
        conn = mysql.connector.connect(user='root', password='mrHDEZ93.', host='127.0.0.1', database='OurWay')
        query = conn.execute("select * from employees where EmployeeId =%d "  %int(employee_id))
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        conn.close()
        return jsonify(result)


api.add_resource(Rutas, '/rutas') # Route_1
api.add_resource(Ubicaciones, '/ubicaciones') # Route_2
api.add_resource(Employees_Name, '/employees/<employee_id>') # Route_3


if __name__ == '__main__':
     app.run()