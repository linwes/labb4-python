import sqlite3
import requests
from flask import Flask, render_template, jsonify, request
from random import randint
import time

def getjson():
    while True:
        time.sleep(10)
        con = sqlite3.connect('väder.db')
        c = con.cursor()

        test = requests.get('http://127.0.0.1:5000/')
        g = test.json()
        c.execute("INSERT INTO väder (regn, snö, värme) VALUES (?,?,?)",g)
        print(g)
        con.commit()
        con.close()
getjson()
