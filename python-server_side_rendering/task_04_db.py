from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

# --- HELPER FUNCTIONS ---

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

def read_sqlite_data():
    try:
        # 1. Connect to database
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        
        # 2. Execute query
        cursor.execute('SELECT id, name, category, price FROM Products')
        rows = cursor.fetchall()
        
        # 3. CONVERT TUPLES TO DICTIONARIES
        # The template expects {'id': 1, 'name': 'Laptop'}
        # But SQL returns (1, 'Laptop')
        products_list = []
        for row in rows:
            product = {
                'id': row[0],
                'name': row[1],
                'category': row[2],
                'price': row[3]
            }
            products_list.append(product)
            
        conn.close()
        return products_list
        
    except sqlite3.Error as e:
        return None # Return None to signal a DB error

# --- ROUTES ---

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
    try:
        with open('items.json', 'r') as f:
            data = json.load(f)
        items_list = data.get('items', [])
        return render_template('items.html', items=items_list)
    except FileNotFoundError:
        return "Items file not found", 404

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    
    products_list = []

    # 1. Fetch Data based on Source
    if source == 'json':
        products_list = read_json_file()
    elif source == 'csv':
        products_list = read_csv_file()
    elif source == 'sql':
        products_list = read_sqlite_data()
        if products_list is None: # Handle DB connection error
             return render_template('product_display.html', error="Database error")
    else:
        return render_template('product_display.html', error="Wrong source")

    # 2. Filter by ID (Shared logic for ALL sources)
    if product_id:
        try:
            p_id = int(product_id)
            filtered_products = [p for p in products_list if p['id'] == p_id]
            
            if not filtered_products:
                return render_template('product_display.html', error="Product not found")
            
            products_list = filtered_products
            
        except ValueError:
            return render_template('product_display.html', error="Invalid ID format")

    return render_template('product_display.html', products=products_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
