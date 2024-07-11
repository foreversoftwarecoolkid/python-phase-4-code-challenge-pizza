#!/usr/bin/env python3

from app import app
from models import db, Restaurant, Pizza, RestaurantPizza

with app.app_context():

    # This will delete any existing rows
    # so you can run the seed file multiple times without having duplicate entries in your database
    print("Deleting data...")
    Pizza.query.delete()
    Restaurant.query.delete()
    RestaurantPizza.query.delete()

    print("Creating restaurants...")
    
    #RESTAURANTS
    
    shack = Restaurant(name="Karen's Pizza Shack", address='address1')
    bistro = Restaurant(name="Sanjay's Pizza", address='address2')
    palace = Restaurant(name="Kiki's Pizza", address='address3')
    pizza_palace = Restaurant(name="Pizza Palace", address='address4')
    tonys_pizzeria = Restaurant(name="Tony's Pizzeria", address='address5')
    mama_mia_pizzeria = Restaurant(name="Mama Mia Pizzeria", address='address6')
    petes_pizza_place = Restaurant(name="Pete's Pizza Place", address='address7')
    luigis_pizza = Restaurant(name="Luigi's Pizza", address='address8')
    vinnys_pizzeria = Restaurant(name="Vinny's Pizzeria", address='address9')
    marios_pizza = Restaurant(name="Mario's Pizza", address='address10')
    giuseppes_pizza = Restaurant(name="Giuseppe's Pizza", address='address11')
    roccos_pizza = Restaurant(name="Rocco's Pizza", address='address12')
    angelos_pizza = Restaurant(name="Angelo's Pizza", address='address13')
    sals_pizza = Restaurant(name="Sal's Pizza", address='address14')
    ginos_pizzeria = Restaurant(name="Gino's Pizzeria", address='address15')
    robertos_pizza = Restaurant(name="Roberto's Pizza", address='address16')
    antonios_pizza = Restaurant(name="Antonio's Pizza", address='address17')
    enzos_pizza = Restaurant(name="Enzo's Pizza", address='address18')
    fabios_pizza = Restaurant(name="Fabio's Pizza", address='address19')
    lucas_pizzeria = Restaurant(name="Luca's Pizzeria", address='address20')

    restaurants = [shack, bistro, palace, pizza_palace, tonys_pizzeria,
                mama_mia_pizzeria, petes_pizza_place, luigis_pizza, vinnys_pizzeria,
                marios_pizza, giuseppes_pizza, roccos_pizza, angelos_pizza,
                sals_pizza, ginos_pizzeria, robertos_pizza, antonios_pizza,
                enzos_pizza, fabios_pizza, lucas_pizzeria]

    print("Creating pizzas...")

    cheese = Pizza(name="Emma", ingredients="Dough, Tomato Sauce, Cheese")
    pepperoni = Pizza(name="Geri", ingredients="Dough, Tomato Sauce, Cheese, Pepperoni")
    california = Pizza(name="Melanie", ingredients="Dough, Sauce, Ricotta, Red peppers, Mustard")
    vegetarian = Pizza(name="Sophia", ingredients="Dough, Tomato Sauce, Cheese, Mushrooms, Onions, Bell peppers")
    meat_lovers = Pizza(name="David", ingredients="Dough, Tomato Sauce, Cheese, Pepperoni, Sausage, Bacon")
    margherita = Pizza(name="Olivia", ingredients="Dough, Tomato Sauce, Mozzarella Cheese, Fresh Basil")
    hawaiian = Pizza(name="Liam", ingredients="Dough, Tomato Sauce, Cheese, Ham, Pineapple")
    buffalo_chicken = Pizza(name="Ava", ingredients="Dough, Buffalo Sauce, Chicken, Cheese, Ranch Dressing")
    four_seasons = Pizza(name="Noah", ingredients="Dough, Tomato Sauce, Mozzarella Cheese, Mushrooms, Artichokes, Ham, Olives")
    bbq_pulled_pork = Pizza(name="Isabella", ingredients="Dough, BBQ Sauce, Pulled Pork, Cheese, Red Onions")

    
    pizzas = [cheese, pepperoni, california,vegetarian,meat_lovers,margherita,hawaiian,buffalo_chicken,four_seasons,bbq_pulled_pork]

    print("Creating RestaurantPizza...")

    pr1 = RestaurantPizza(restaurant=shack, pizza=cheese, price=1)
    pr2 = RestaurantPizza(restaurant=bistro, pizza=pepperoni, price=4)
    pr3 = RestaurantPizza(restaurant=palace, pizza=california, price=5)
    pr4 = RestaurantPizza(restaurant=pizza_palace, pizza=vegetarian, price=3)
    pr5 = RestaurantPizza(restaurant=tonys_pizzeria, pizza=meat_lovers, price=6)
    pr6 = RestaurantPizza(restaurant=mama_mia_pizzeria, pizza=margherita, price=3)
    pr7 = RestaurantPizza(restaurant=petes_pizza_place, pizza=hawaiian, price=4)
    pr8 = RestaurantPizza(restaurant=luigis_pizza, pizza=buffalo_chicken, price=5)
    pr9 = RestaurantPizza(restaurant=vinnys_pizzeria, pizza=four_seasons, price=5)
    pr10 = RestaurantPizza(restaurant=marios_pizza, pizza=bbq_pulled_pork, price=6)

    restaurantPizzas = [pr1, pr2, pr3, pr4, pr5, pr6, pr7, pr8, pr9]
    db.session.add_all(restaurants)
    db.session.add_all(pizzas)
    db.session.add_all(restaurantPizzas)
    db.session.commit()

    print("Seeding done!")