from flask import Flask, render_template, request
import csv
import random

next_route = 'greeting'
text_name = 'name'

app = Flask(__name__)

@app.route('/')
def root():
    #print request.method
    return render_template('form.html', route=next_route, input_type=text_name)

@app.route('/' + next_route)
def greeting():
    user = request.args[text_name]
    method_used = request.method
    return render_template('greeting.html', name=user, method=method_used)
    
if __name__ == '__main__':
    app.debug = True
    app.run()