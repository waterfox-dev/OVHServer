from flask import Flask, render_template, redirect, jsonify, request, url_for
from flask.wrappers import Request

from datetime import date, datetime
from router import routingdic


import json


app = Flask(__name__)

@app.route("/dpc") 
def dpc_homepage():
    return render_template(routingdic['chat-homepage'], messages = json.load(open('data/messages.json', encoding='UTF8')))

@app.route('/dpc_publish', methods = ['GET', 'POST'])
def dpc_publish():
    
    data = dict(request.form)
    today = date.today()
    now = datetime.now()
    
    if data['message'] == '!clear' : 
        
        with open("data/messages.json", 'r', encoding='UTF8') as r_file :
            r_file = json.load(r_file)
            r_file = []
            with open("data/messages.json", 'w', encoding='UTF8') as w_file :
                json.dump(r_file, w_file)
                
    else :
        
        with open("data/messages.json", 'r', encoding='UTF8') as r_file :
            r_file = json.load(r_file)
            try :
                r_file.append(
                    {
                        "id" : r_file[-1]['id'] + 1,
                        "author" : data['author'], 
                        "content" : data['message'],
                        "date" : today.strftime("%d-%m-%Y"),
                        "hour" : now.strftime("%H:%M")
                    }
                )
            except IndexError :
                r_file.append(
                    {
                        "id" : 0,
                        "author" : data['author'], 
                        "content" : data['message'],
                        "date" : today.strftime("%d-%m-%Y"),
                        "hour" : now.strftime("%H:%M")
                    }
                )    
            
            with open("data/messages.json", 'w', encoding='UTF8') as w_file :
                json.dump(r_file, w_file)
                
    return redirect(url_for('dpc_homepage'))
app.run()