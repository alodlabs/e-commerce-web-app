from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from .models import Product, Order
from . import db

main_bp = Blueprint('main', __name__)

@main_bp.route("/")
def index():
    products = Product.query.all()
    return render_template("index.html", products=products)

@main_bp.route("/admin")
def admin():
    products = Product.query.all()
    return render_template("admin.html", products=products)

@main_bp.route("/admin/add", methods=["POST"])
def add_product():
    data = request.form
    new_product = Product(
        name=data['name'],
        description=data['description'],
        price=float(data['price']),
        stock=int(data['stock']),
        image_url=data['image_url']
    )
    db.session.add(new_product)
    db.session.commit()
    return redirect(url_for('main.admin'))

@main_bp.route("/cart", methods=["GET", "POST"])
def cart():
    if request.method == "GET":
        return render_template("cart.html")
    # Handle checkout logic
