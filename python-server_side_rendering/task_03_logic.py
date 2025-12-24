from flask import Flask, render_template
from flask import request
import json
import csv

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    with open('items.json', 'r') as f:
        data = json.load(f)
    items_list = data.get('items', [])
    return render_template('items.html', items=items_list)

@app.route('/query_example')
def query_example():
    request
    source = request.args.get('source')
    return request.query_string
    #return render_tempplate("product_display.html")
    if request.query_string == 'json':
        f = open('products.json',)
        data = json.load(f)
        for i in data:
            print(i)
        f.close()
    elif request.query_string == 'csv':
        with open('products.csv', mode='r') as file:
            csvfile = csv.reader(file)
            for lines in csvfile:
                print(lines)

                """
                args1 = request.args['args1']
    args2 = request.args['args2']
    args3 = request.args['args3']
"""

if __name__ == '__main__':
    app.run(debug=True, port=5000)
