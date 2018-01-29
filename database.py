# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 22:05:42 2018

@author: dgmcl
"""

import sqlite3
import pandas as pd

def create_database():
    '''Creates a new database and table for holding the car data'''

    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("CREATE TABLE cars (make TEXT, model TEXT, year INTEGER, chassis_id TEXT, id INTEGER, last_updated TEXT, price REAL)")
    conn.close()
    
def data_entry():
    '''Reads in the provided data from the assignment sheet that had been saved in csv format and populates the table'''

    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    data = pd.read_csv("cars.csv")
    
    entries = []
    for r in data.iterrows():
        i, d = r
        d = tuple(d)
        entries.append(d)
        
    c.executemany("INSERT INTO cars VALUES (?,?,?,?,?,?,?)", entries )
    conn.commit()
    conn.close()

'''running the functions to create database, table and populate it'''
create_database()
data_entry()
    

    

    


