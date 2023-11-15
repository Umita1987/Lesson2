from django.shortcuts import render


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

