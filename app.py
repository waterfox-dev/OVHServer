from flask import Flask, render_template, redirect, jsonify
from router import routingdic

app = Flask(__name__)

@app.route("/dpc") 
def dpc_homepage():
    return render_template(routingdic['chat-homepage'])


app.run()