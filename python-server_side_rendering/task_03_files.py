from flask import Flask, render_template
from flask import request
import json
import csv

app = Flask(__name__)

def read_json_file():
    try:
        with open('products.json', 'r') as f:
            return json.load(f)
        except FileNotFoundError:
            return []

def read_csv_file():
    data = []
    try:
        with open('products.csv', 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                data.append(row)
            return data
        except FileNotFoundError:
            return []

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

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source == 'json':
        product_list = read_json_file()
    elif source == 'csv':
        product_list = read_csv_file() 
    else:
        return render_template('product_display.html', error="Wrong source")

    if product_id:
        try:
            p_id = int(product_id)
            filtered_products = [p for p in products_list if p['id'] == p_id]
            if not filtered_products:
                return render_template('product_display.html', error="Product was not found")

            products_list = filtered_products

        except ValueError:
            return render_template('product_display.html', error="Invalid ID format")


    return render_template('product_display.html', products=products_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
