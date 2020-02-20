import sqlite3
from flask import Flask, escape, request, jsonify, render_template
from random import randint
import requests
import time
app = Flask(__name__)
# conn = sqlite3.connect('väder.db')
# c = conn.cursor()
# c.execute("""CREATE TABLE väder(
#     regn text,
#     snö text,
#     värme text
#     )""")
# con.commit()
# con.close()
@app.route('/')
def läggIn():
    regn = randint(1,100)
    snö= randint(1,100)
    värme = randint(-30,40)
    while True:
        time.sleep(10)
        return jsonify(regn, snö, värme)

if __name__ :
    app.debug = True
    app.run(host= '127.0.0.1', port=5000)