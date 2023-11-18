from django.http import HttpResponse
from django.shortcuts import render
from App1.models import Item

def hello(request, item_id):
    items = [
        {"id": 1, "name": "Кроссовки abibas", "quantity": 5},
        {"id": 2, "name": "Куртка кожаная", "quantity": 2},
        {"id": 5, "name": "Coca-cola 1 литр", "quantity": 12},
        {"id": 7, "name": "Картофель фри", "quantity": 0},
        {"id": 8, "name": "Кепка", "quantity": 124},
    ]
    result = {}
    for el in items:
        if el["id"] == item_id:
            result["id"] = el["id"]
            result["name"] = el["name"]
            result["quantity"] = el["quantity"]
            break
    return render(request, "1.html", result)


def list_of_products(request):
    items = [
        {"id": 1, "name": "Кроссовки abibas", "quantity": 5},
        {"id": 2, "name": "Куртка кожаная", "quantity": 2},
        {"id": 5, "name": "Coca-cola 1 литр", "quantity": 12},
        {"id": 7, "name": "Картофель фри", "quantity": 0},
        {"id": 8, "name": "Кепка", "quantity": 124},
    ]
    return render(request, "2.html", {"items": items})


def main_page(request):
    return render(request, "Main.html")


def about(request):
    return render(request, "about.html")


def fill(request):
    item = Item(name="Milk", quantity=5)
    item = Item(name="Eggs", quantity=10)
    item.save()
    return HttpResponse("Successfull")


def create_item(request):
    item = Item(name="Milk", quantity=5, price=500)
    item.save()
    result = f"{item.name} Quantity {item.quantity} Price {item.price} "
    return HttpResponse(result)


def read_item(request, item_id):
    item = Item.objects.filter(id=item_id).first()
    result = f"{item.name} Quantity {item.quantity} Price {item.price} "
    return HttpResponse(result)


def update_item(request, item_id):
    item = Item.objects.filter(id=item_id).first()
    item.name = "Nails"
    item.save()
    result = f"Name {item.name}  Quantity {item.quantity}  Price {item.price} "
    return HttpResponse(result)


def delete_item(request, item_id):
    item = Item.objects.filter(id=item_id).first()
    item.delete()
    return HttpResponse("Successfull")
