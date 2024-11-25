from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Mock data for products
mock_products = [
    {
        "id": 1,
        "name": "Product 1",
        "description": "This is a great product.",
        "price": 10.99,
        "stock": 5,
        "image_url": "/static/images/placeholder.png",
    },
    {
        "id": 2,
        "name": "Product 2",
        "description": "Another awesome product.",
        "price": 19.99,
        "stock": 3,
        "image_url": "/static/images/placeholder.png",
    },
]

@app.route("/")
def index():
    return render_template("index.html", products=mock_products)

@app.route("/product/<int:product_id>")
def product_detail(product_id):
    product = next((p for p in mock_products if p["id"] == product_id), None)
    if not product:
        return "Product not found", 404
    return render_template("product.html", product=product)

@app.route("/admin")
def admin():
    return render_template("admin.html", products=mock_products)

if __name__ == "__main__":
    app.run(debug=True)
