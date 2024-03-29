from flask import Flask, redirect, request, render_template
import sqlalchemy as db
from sqlalchemy import text

app = Flask(__name__)
engine = db.create_engine('sqlite:///face.db')

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        product_type = request.form.get('product_type') 
        skin_type = request.form.get('skin_type')
        if product_type == "Product Type" and skin_type == "Skin Type":
            return redirect('/list')
        
        connection = engine.connect()
        query = text("SELECT product_type, skin_type, brand, name, price FROM face_product WHERE product_type LIKE :product_type AND (skin_type LIKE :skin_type OR skin_type LIKE '%All%')")
        result = connection.execute(query, {'product_type': f'%{product_type}%', 'skin_type': f'%{skin_type}%'})

        rows = []
        for row in result.fetchall():
            rows.append({'product_type': row[0], 'skin_type': row[1], 'brand': row[2], 'name': row[3], 'price': row[4]})
        if len(rows) == 0: 
            return render_template('sorry.html')
        else:
            return render_template('yourproducts.html', result=rows)

    return render_template('index.html')

@app.route("/list")
def list():
    connection = engine.connect()
    query = text("SELECT product_type, skin_type, brand, name, price FROM face_product")
    result = connection.execute(query)

    rows = []
    for row in result.fetchall():
        rows.append({'product_type': row[0], 'skin_type': row[1], 'brand': row[2], 'name': row[3], 'price': row[4]})
    return render_template("list.html", result = rows)

@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/add")
def add():
    if request.method == 'GET':
        product_type = request.form.get('product_type') 
        skin_type = request.form.get('skin_type')
        name = request.form.get('productname')
        price = request.form.get('price')
        brand = request.form.get('brand')
        
        connection = engine.connect()
        query = text("INSERT INTO face_product (product_type,skin_type,brand,name,price) VALUES (:product_type,:skin_type,:brand,:name,:price)")
        result = connection.execute(query, {'product_type': f'%{product_type}%', 'skin_type': f'%{skin_type}%', 'name': f'%{name}%', 'brand': f'%{brand}%', 'price': f'%{price}%'})

    return render_template("add.html")

if __name__ == "__main__":
    app.run(port=8000, debug=True)
