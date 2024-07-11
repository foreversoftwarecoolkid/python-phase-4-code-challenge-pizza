#!/usr/bin/env python3
from models import db, Restaurant, RestaurantPizza, Pizza
from flask_migrate import Migrate
from flask import Flask, request, make_response,jsonify
from flask_restful import Api, Resource
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE = os.environ.get("DB_URI", f"sqlite:///{os.path.join(BASE_DIR, 'app.db')}")

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

api = Api(app)


@app.route("/")
def index():
    return "<h1>Code challenge</h1>"


# FETCH ALL RESTAURANTS
@app.route('/restaurants', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()
    restaurant_list = [{
        "address": restaurant.address,
        "id": restaurant.id,
        "name": restaurant.name,
        # "pizzas": [pizza.to_dict() for pizza in restaurant.pizzas]
    } for restaurant in restaurants]
    return jsonify(restaurant_list), 200








#FETCH RESTAURANT BY ID
@app.route('/restaurants/<int:id>', methods=['GET'])
def get_restaurant(id):
    restaurant = Restaurant.query.get_or_404(id)
    if restaurant is None:
        return jsonify({"error": "restaurant not found"}), 404
    return jsonify({
        "address": restaurant.address,
        "id": restaurant.id,
        "name": restaurant.name,
        "restaurant_pizzas": [pizza.to_dict() for pizza in restaurant.restaurant_pizzas]
    }), 200







#DELETE RESTAURANT BT ID
@app.route('/restaurants/<int:id>', methods=['DELETE'])
def delete_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if restaurant is None:
        return jsonify({"error": "Restaurant not found"}), 404

    db.session.delete(restaurant)
    db.session.commit()
    return jsonify({"success": "restaurant deleted successfully"}), 200






# FETCH ALL PIZZAS
@app.route('/pizzas', methods=['GET'])
def get_pizzas():
    pizzas = Pizza.query.all()
    pizza_list = [{
        "id": pizza.id,
        "ingredients": pizza.ingredients,
        "name": pizza.name,
    } for pizza in pizzas]
    return jsonify(pizza_list), 200






# Route to create a new RestaurantPizza
@app.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    data = request.get_json()

    # Extract data from request JSON
    price = data.get('price')
    pizza_id = data.get('pizza_id')
    restaurant_id = data.get('restaurant_id')

    # Validate required fields
    if not all([price, pizza_id, restaurant_id]):
        return jsonify({"error": "Missing required fields"}), 400

    try:
        # Query for pizza and restaurant objects
        pizza = Pizza.query.get_or_404(pizza_id)
        restaurant = Restaurant.query.get_or_404(restaurant_id)

        # Create a new RestaurantPizza instance
        new_restaurant_pizza = RestaurantPizza(
            price=price,
            pizza=pizza,
            restaurant=restaurant
        )

        # Add to database session and commit
        db.session.add(new_restaurant_pizza)
        db.session.commit()

        # Return JSON response with the created RestaurantPizza data
        return jsonify({
            "id": new_restaurant_pizza.id,
            "pizza": {
                "id": pizza.id,
                "name": pizza.name,
                "ingredients": pizza.ingredients
            },
            "pizza_id": pizza.id,
            "price": new_restaurant_pizza.price,
            "restaurant": {
                "id": restaurant.id,
                "name": restaurant.name,
                "address": restaurant.address
            },
            "restaurant_id": restaurant.id
        }), 201

    except Exception as e:
        # Rollback the session in case of any exception
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
    
    
if __name__ == "__main__":
    app.run(port=5000, debug=True)