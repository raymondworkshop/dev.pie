import os

from flask import Flask, render_template, request, jsonify
from chat_can import get_conversation
#from chat import translator


# Initializing flask app
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route('/get')
def get_messages():
    userText = request.args.get('msg')
    #en_userText = translator('zh', 'en', userText)
    #print(userText)
    response = get_conversation(userText)
    print(response)
    return response

     
# Running app
if __name__ == '__main__':
    app.run(DEBUG=True,threaded=True)
    #app.run(host='144.214.20.231',debug=True, threaded=True)