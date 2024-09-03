import os

from flask import Flask, render_template, request, jsonify
from chat import get_conversation
#from chat import translator


# Initializing flask app
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route('/get')
def get_messages():
    userText = request.args.get('msg')
    #en_userText = translator('zh', 'en', userText)
    response = get_conversation(userText)
    #print(response)
    return response

     
