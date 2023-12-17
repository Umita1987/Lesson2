from django.http import HttpResponse
from django.shortcuts import render

from App1.models import Item, Image
from .forms import ImageForm


def hello(request, item_id):
    items = items = [
        {"id": 1, "name": "Кроссовки abibas", "quantity": 5, "price": 2500,
         "image": "https://bugbytes-django-s3-demo.s3.eu-north-1.amazonaws.com/photos/2023/11/28/adidas_yLYGDs0.jpg"},
        {"id": 2, "name": "Куртка кожаная", "quantity": 2, "price": 4500,
         "image": "https://bugbytes-django-s3-demo.s3.eu-north-1.amazonaws.com/photos/2023/11/26/%D0%BA%D1%83%D1%80%D1%82%D0%BA%D0%B01.jpg"},
        {"id": 5, "name": "White T-shirt", "quantity": 5, "price": 2500,
         "image": "https://bugbytes-django-s3-demo.s3.eu-north-1.amazonaws.com/photos/2023/11/28/white_t-shirt.jpg"},
        {"id": 7, "name": "Vintage pink dress", "quantity": 0, "price": 5500,
         "image": "https://bugbytes-django-s3-demo.s3.eu-north-1.amazonaws.com/photos/2023/11/28/pink_dress.jpg"},
        {"id": 8, "name": "Кепка", "quantity": 124, "price": 1500, "image": "https://bugbytes-django-s3-demo.s3.eu-north-1.amazonaws.com/photos/2023/11/27/%D0%BA%D0%B5%D0%BF%D0%BA%D0%B0.jpg"},
    ]
    result = {}
    for el in items:
        if el["id"] == item_id:
            result["id"] = el["id"]
            result["name"] = el["name"]
            result["quantity"] = el["quantity"]
            result["price"] = el["price"]
            result["image"] = el["image"]
            break
    return render(request, "1.html", result)


def list_of_products(request):
    items = [
        {"id": 1, "name": "Кроссовки abibas", "quantity": 5, "price": 2500,
         "image": "https://bugbytes-django-s3-demo.s3.eu-north-1.amazonaws.com/photos/2023/11/28/adidas_yLYGDs0.jpg"},
        {"id": 2, "name": "Куртка кожаная", "quantity": 2, "price": 4500,
         "image": "https://bugbytes-django-s3-demo.s3.eu-north-1.amazonaws.com/photos/2023/11/26/%D0%BA%D1%83%D1%80%D1%82%D0%BA%D0%B01.jpg"},
        {"id": 5, "name": "White T-shirt", "quantity": 5, "price": 2500,
         "image": "https://bugbytes-django-s3-demo.s3.eu-north-1.amazonaws.com/photos/2023/11/28/white_t-shirt.jpg"},
        {"id": 7, "name": "Vintage pink dress", "quantity": 0, "price": 5500,
         "image": "https://bugbytes-django-s3-demo.s3.eu-north-1.amazonaws.com/photos/2023/11/28/pink_dress.jpg"},
        {"id": 8, "name": "Кепка", "quantity": 124, "price": 1500, "image": "https://bugbytes-django-s3-demo.s3.eu-north-1.amazonaws.com/photos/2023/11/27/%D0%BA%D0%B5%D0%BF%D0%BA%D0%B0.jpg"},
    ]
    return render(request, "product.html", {"items": items})


def main_page(request):
    return render(request, "Main.html")


def about(request):
    return render(request, "about.html")

def contacts(request):
    return render(request, "contacts.html")
def image_upload_view(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'index.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'index.html', {'form': form})


def display_images(request):
    if request.method == "GET":
        Images = Image.objects.all()
        return render(request, "display_images.html", {"images": Images})
