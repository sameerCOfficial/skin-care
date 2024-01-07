from flask import Flask, request, render_template
import sqlalchemy as db
from sqlalchemy import text

app = Flask(__name__)
engine = db.create_engine('sqlite:///face.db')

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        product_type = request.form.get('product_type') 
        skin_type = request.form.get('skin_type')
        
        connection = engine.connect()
        query = text("SELECT product_type, skin_type, brand, name, price FROM face_product WHERE product_type = :product_type AND skin_type = :skin_type")
        result = connection.execute(query, {'product_type': product_type, 'skin_type': skin_type})

        if result.rowcount == 0:  # Check if no rows were returned
            return render_template('sorry.html')
        else:
            # Assuming only one row is returned for simplicity
            row = result.fetchone()
            product_type = row[0]
            skin_type = row[1]
            brand = row[2]
            name = row[3]
            price = row[4]
            return render_template('yourproducts.html', product_type=product_type, skin_type=skin_type, brand=brand, name=name, price=price)

    return render_template('index.html')

@app.route("/list")
def list():
    return render_template("list.html")

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(port=8000, debug=True)
