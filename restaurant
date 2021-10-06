#!/bin/python3

import math
import os
import random
import re
import sys

menu = {'St. Emilion': 18
, 'Pickles': 10
, 'Pomard': 5
, 'Sliced Bananas': 15
, 'Apple Sauce': 20
, 'Salted Almonds': 10
, 'Young Onions': 10
, 'Browned Potatoes': 20
, 'Consomme In Cup': 20
, 'Mashed Potatoes': 15
, 'Ice Cream': 20
, 'Baked Apples With Cream': 20
, 'Stewed Prunes': 20
, 'Pot Of Chocolate': 20
, 'French Rolls': 5
, 'Boiled Eggs': 20
, 'Fish Cakes': 15
, 'Oatmeal': 20
, 'Baked Apples': 20
, 'Lady Fingers': 15
, 'Demi-Tasse': 15
, 'Vve Cliquot': 7
, 'Plain Omelette': 15
, 'Fried Flounders': 15
, 'Queen Olives': 15
, 'Chow Chow': 20
, 'Spinach With Egg': 20
, 'Boiled Potatoes': 20
, 'Crackers': 10
, 'Fried Eggs': 20
, 'Roast Veal': 20
, 'Porterhouse Steak': 5
, 'Hamburger Steak': 20
, 'Fried Liver': 10
, 'Stewed': 15
, 'Grilled Ham': 5.5
, 'Poached Eggs On Toast': 20
, 'Dry Toast': 10
, 'Buckwheat Cakes': 20
, 'Stewed Tripe': 10
, 'Corn Bread': 10
, 'Beef Stew': 15
, 'Tomato Soup': 10
, 'Fruit In Season': 20
, 'Ham Omelette': 15
, 'Saute': 15
, 'Eggs, Boiled': 20
, 'Shirred Eggs': 19
, 'Rice Cakes': 20
, 'Liver And Bacon': 15
, 'Fried Chicken A La Maryland': 5.6
, 'Stilton Cheese': 10
, 'Broiled Lamb Chops': 5.25
, 'Wheat Cakes': 15
, 'Dipped Toast': 15
, 'Coffee Cake': 5
, 'Potatoes': 15
, 'Moet & Chandon, Brut': 5
, 'Lemon Soda': 10
, 'Roast Duck': 15.25
, 'Cabbage': 20
, 'Blackberry Pie': 5
, 'Fried Potatoes': 15
, 'Stewed French Prunes': 5
, 'Sliced Bananas With Cream': 10
, 'Buttered Toast': 15
, 'Tomatoes': 15
, 'Baked Potatoes': 20
, 'Beefsteak': 15
, 'Sardellen': 15
, 'Plum Tart': 6
, 'Vermouth': 20
, 'Gilka Kummel': 15
, 'Milk Punch': 15
, 'Claret Punch': 15
, 'Porridge': 20
, 'Roast Capon': 6
, 'Sweet Pickles': 20
, 'Saute Potatoes': 20
, 'Oporto': 11.25
, 'Lemonade': 12
, 'Mumm, Extra Dry': 8
, 'Chablis': 14
, 'Barbera': 5
, 'Barolo': 12
, 'Capri': 5
, 'Cup Of Clam Broth': 20
, 'Chateau Margaux': 17
, 'Tea, Pot': 20
, 'Pudding': 10
, 'Fruits': 10
, 'Buttermilk': 10
, 'Hashed Browned Potatoes': 20
, 'Assorted Cake': 20
, 'Oysters, Half Shell': 10
, 'Little Neck Clams, Half Shell': 20
, 'Orange Bitters': 15
, 'Creme Yvette': 15
, 'Maraschino': 20
, 'Benedictine': 20
, 'Absinthe': 20
, 'Creme De Menthe': 15
, 'Kirschwasser': 15
, 'Sarsaparilla': 5
, 'Marcobrunner': 5
, 'Ruedesheimer Berg': 18.25
, 'Port': 6
, 'Burgundy': 8
, 'Cockburn': 5
, 'Vino De Pasto': 14.75
, 'Amontillado': 20
, 'Barsac': 10.5
, 'Clos De Vougeot': 6
, 'Chateau Leoville': 18.5
, 'Chateau La Rose': 15
, 'St. Julien (Barton & Guestier)': 12
, 'G. H. Mumm & Co., Extra Dry': 5.5
, 'Dry Monopole': 16
, 'Rice': 10
, 'English Pheasant': 5
, 'Sweet Corn': 10
, 'Peach Pie': 15
, 'Cherry Tarts': 20
, 'Vanilla Eclairs': 10}

def restaurant(MENU):
    total = 0
    orders = []
    
    while True:
        new_order = input("Order: ")
        if new_order in MENU:
            orders.append(new_order)
            total += MENU[new_order]
        elif new_order == "":
            receipt = ""
            for order in orders:
                receipt += f"{order} is {MENU[order]}\n"
            receipt += f"Your total is {total}"
            return receipt

if __name__ == '__main__':
    print(restaurant(menu))