from django.shortcuts import render
from django.http import HttpResponse

def Homeview(request):
    content={"page":"Home"}
    return render(request,"Home.html",context=content)

def Loginview(request):
    content={"page":"Login"}
    return render(request,"Login.html",context=content)

def Viewmenu(request):
    content = {"page":"Menu"}
    dishes =[
        {"Dish":"Pizza","Description": "Delicious pizza with various toppings", "Price": 10},
        {"Dish":"Burger","Description": "Juicy burger with fresh ingredients", "Price": 8},
        {"Dish":"Pasta","Description": "Creamy pasta with rich sauce", "Price": 12},
        {"Dish":"Salad","Description": "Healthy salad with fresh vegetables", "Price": 7},
        {"Dish":"Sushi","Description": "Fresh sushi rolls with various fillings", "Price": 15},
        {"Dish":"Steak","Description": "Grilled steak cooked to perfection", "Price": 20},
        {"Dish":"Tacos","Description": "Spicy tacos with flavorful fillings", "Price": 9},
        {"Dish":"Ice Cream","Description": "Creamy ice cream in various flavors", "Price": 5},
    ]
    content["dishes"] = dishes
    return render(request,"Menu.html",context=content)