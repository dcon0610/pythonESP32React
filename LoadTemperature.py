
from re import X
from sqlite3 import Date
from venv import create
from flask import Flask, g, jsonify
from flask_cors import CORS
import requests
import DatabaseConfig as db
import json
from datetime import datetime, timedelta
import time
from multiprocessing import Process, Value
import plotly.express as px
import psycopg2.extras
import plotly.io as pio

pio.kaleido.scope.default_format="svg"

dbCursor = db.cursor(cursor_factory = psycopg2.extras.RealDictCursor)

app = Flask(__name__)
cors = CORS(app)

@app.route("/api/test")
def test_app():
    response = jsonify(message="Simple server is running")
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route("/api/testpost", methods = ['POST'])
def test_app_post():
    response = jsonify(message="Simple server is running")
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response
@app.route("/api/temperature")
def return_temperature():
    try:
        sql = "select time, temperature from TemperatureRecords;"
        dbCursor.execute(sql)
        temperatureData = dbCursor.fetchall()
        temperatureDict = dict( time = [], temperature =[])
        print("gpt tp jere")
        for row in temperatureData:
            
            temperatureDict["time"].append((row['time']))
            temperatureDict["temperature"].append(row['temperature'])
        return temperatureDict
    except Exception as e:
        print(e)
        return(str(e))

def create_svg(df):
    fig = px.line(df, x="time", y="temperature", title='soil temp')
    fig.update_xaxes(dtick=60*60*24)
    fig.update_yaxes(range=[-5, 50])
    img_bytes = fig.to_image(format="svg")
    return img_bytes

def get_temperature():
    while(True):
        try: 
            url = "http://4e43-27-33-189-105.ngrok.io/temperature"
            r = requests.get(url)
            tempData = json.loads(r.content.decode('UTF-8'))
            temperature = tempData.get('value')
            
            date = datetime.now()
        

            sql = '''insert into TemperatureRecords(time, temperature)
            VALUES(%s, %s);'''
            dbCursor.execute(sql,(date, temperature))


            print(tempData.get('value'))
        except Exception as e:
            print(e)
        db.conn.commit()
        time.sleep(10*60)

p = Process(target=get_temperature)
p.start()
if __name__ == '__main__':
   app.run(port=9566)
    # run() method of Flask class runs the application 
    # on the local development server.

