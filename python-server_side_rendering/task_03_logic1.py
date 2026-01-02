from flask import Flask, render_template
from flask import request
import json

app = Flask(__name__)

def table():
    return render_template('product_display.html', headings=headings, data=data)

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
    id = request.args.get('id')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
