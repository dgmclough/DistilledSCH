# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 22:05:42 2018

@author: dgmcl
"""

import sqlite3
import json
from datetime import datetime
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    '''Renders a welcome message to index or home page'''

    return "Welcome to Dara's Application"

@app.route('/car/', methods = ['GET', 'POST'])
def car():
    '''Differentiates between two different HTTP Requests. 1) A GET request for all of the cars in the database.
    2) A POST request that attempts to submit car details into the database'''

    if (request.method == 'GET'):
        try:
            conn = sqlite3.connect('database.db')
	    conn.row_factory = sqlite3.Row
            c = conn.cursor()
	    c.execute("SELECT make, model, year, id, last_updated, price FROM cars")
	    data = c.fetchall()
            output = []
            for row in data:
                d = dict(zip(row.keys(), row))
                output.append(d)
            return json.dumps(output, sort_keys=True, indent=4, separators=(',', ': '))
        except Exception as e:
            return "Sorry, there was an error"
        conn.close()
        
    elif (request.method == 'POST'):
        try:
            conn = sqlite3.connect('database.db')
            c = conn.cursor()
	    data = request.data
	    dataDict = json.loads(data)
	    make = dataDict.get('make', None)
            model = dataDict.get('model', None)
            year = dataDict.get('year', None)	
	    year = int(year) 
	    last_updated = str(datetime.now())
            chassis_id = dataDict.get('chassis_id', None)
	    c.execute("SELECT MAX(id) + 1 FROM cars")
	    cid = c.fetchone()[0]
	    price = dataDict.get('price', None)
	    row = (make, model, year, chassis_id, cid, last_updated, price)
	    c.execute("INSERT INTO cars VALUES (?,?,?,?,?,?,?)", row)
	    conn.commit()
            return "Successful Entry"
        except Exception as e:
            return "Sorry, there was an error with the data you have tried to input"
	conn.close()
	

@app.route('/car/<id>', methods = ['GET'] )
def car_id(id):
    '''Accepts GET requests with the specific car id as a variable in the URL. Only renders rows
    from the database that match with the supplied id'''

    try:
        conn = sqlite3.connect('database.db')
        conn.row_factory = sqlite3.Row
        c = conn.cursor()
        c.execute("SELECT make, model, year, id, last_updated, price  FROM cars WHERE id = ?", (id))
        data = c.fetchall()
        output = []
        for row in data:
            d = dict(zip(row.keys(), row))
            output.append(d)
        return json.dumps(output, sort_keys=True, indent=4, separators=(',', ': '))
    except Exception as e:
	return "Sorry, there was an error"
    conn.close()
    

@app.route('/avgprice/', methods = ['POST'])
def avgprice():
    '''Accepts a POST request and finds the average value for the price of the car according to the details
    submitted'''

    try:
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        data = request.data
        dataDict = json.loads(data)
        make = dataDict.get('make', None)
        model = dataDict.get('model', None)
        year = dataDict.get('year', None)
        row = (make, model, year)
        c.execute("SELECT avg(price) FROM cars WHERE make = ? AND model = ? AND year = ?", (make, model, year))
        avg = c.fetchone()[0]
        output = {}
        output["Avg_price"] = avg
        return json.dumps(output)
    except Exception as e:
	return "Sorry, there was an error"
    conn.close()

if __name__ == '__main__':
    app.run(host= "0.0.0.0")
