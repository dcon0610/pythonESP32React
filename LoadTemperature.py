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
    sql = "select time, temperature from TemperatureRecords where id < %s"
    dbCursor.execute(sql, (700000,))
    temperatureData = dbCursor.fetchall()
    temperatureDict = dict( time = [], temperature =[])
    for row in temperatureData:
        
        temperatureDict["time"].append((row['time']).strftime("%x %X"))
        temperatureDict["temperature"].append(row['temperature'])
    fig = create_svg(temperatureDict)
    return fig

def create_svg(df):
    fig = px.line(df, x="time", y="temperature", title='soil temp')
    fig.update_xaxes(nticks=5)
    fig.update_yaxes(range=[10, 30])
    img_bytes = fig.to_image(format="svg", width=1500, height=1000)
    return img_bytes

def get_temperature():
    while(True):
        try: 
            url = "https://b324-27-33-189-105.ngrok.io/temperature"
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
if __name__ == '__main__':

    p = Process(target=get_temperature)
    p.start()


    # run() method of Flask class runs the application 
    # on the local development server.
    app.run(threaded = True, debug=True, use_reloader=False)






