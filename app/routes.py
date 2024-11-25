from flask import Blueprint, render_template, request, redirect, url_for
from .models import Product
from . import db, socketio

main_bp = Blueprint("main", __name__)

@main_bp.route("/")
def index():
    products = Product.query.all()
    return render_template("index.html", products=products)

@main_bp.route("/product/<int:product_id>")
def product_detail(product_id):
    product = Product.query.get_or_404(product_id)
    return render_template("product.html", product=product)

@main_bp.route("/admin", methods=["GET", "POST"])
def admin():
    if request.method == "POST":
        name = request.form.get("name")
        description = request.form.get("description")
        price = request.form.get("price")
        stock = request.form.get("stock")
        image_url = request.form.get("image_url", "/static/images/placeholder.png")

        new_product = Product(
            name=name, description=description, price=float(price), stock=int(stock), image_url=image_url
        )
        db.session.add(new_product)
        db.session.commit()

        return redirect(url_for("main.admin"))
    products = Product.query.all()
    return render_template("admin.html", products=products)

@main_bp.route("/chat")
def chat():
    return render_template("chat.html")

@socketio.on("message")
def handle_message(data):
    socketio.emit("message", data, broadcast=True)
