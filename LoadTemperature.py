from re import X
from sqlite3 import Date
from venv import create
from flask import Flask, g
import requests
import DatabaseConfig as db
import json
from datetime import datetime
import time
from multiprocessing import Process, Value
import plotly.express as px
import psycopg2.extras

dbCursor = db.cursor(cursor_factory = psycopg2.extras.RealDictCursor)

app = Flask(__name__)

@app.route("/temperature")
def return_temperature():
    try:
        sql = "select time, temperature from TemperatureRecords "
        print("started")
        print(dbCursor)
        dbCursor.execute(sql)
        print("Execution complete")
        temperatureData = dbCursor.fetchall()
        print("fetchall complete")
        temperatureDict = dict( time = [], temperature =[])
        for row in temperatureData:
            
            temperatureDict["time"].append((row['time']).strftime("%x %X"))
            temperatureDict["temperature"].append(row['temperature'])
        fig = create_svg(temperatureDict)
        return fig
    except Exception as e:
        print(repr(e))
        return("exception")


def create_svg(df):
    fig = px.line(df, x="time", y="temperature", title='soil temp')
    fig.update_xaxes(nticks=5)
    fig.update_yaxes(range=[10, 30])
    img_bytes = fig.to_image(format="svg", width=1500, height=1000)
    return img_bytes

if __name__ == '__main__':

 

    # run() method of Flask class runs the application 
    # on the local development server.
    app.run(host='0.0.0.0')






