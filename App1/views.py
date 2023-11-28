from django.http import HttpResponse
from django.shortcuts import render

from App1.models import Item, Image
from .forms import ImageForm


def hello(request, item_id):
    items = [
        {"id": 1, "name": "Кроссовки abibas", "quantity": 5, "price": 2500,
         "image": "/media/photos/2023/11/23/adidas.jpg"},
        {"id": 2, "name": "Куртка кожаная", "quantity": 2, "price": 4500,
         "image": "https://bugbytes-django-s3-demo.s3.eu-north-1.amazonaws.com/photos/2023/11/26/%D0%BA%D1%83%D1%80%D1%82%D0%BA%D0%B01.jpg?response-content-disposition=inline&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCmV1LW5vcnRoLTEiRjBEAiBFrpKUPU%2FIYoUqPHDny9CuduJLcArOuJLtom90kzn0cQIgaUzY%2B4LuW6mqt6aImr%2B9WTJujegdHKuHeDxe3enXXc4q7QIItv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw4MzY5MzcxODE5NTkiDMveadTVTknVR03ORCrBAmNkxYUb6gVC1LJd9a5pVWLc9HFiPFwi3XBMwhKY%2FMquC1CtI4GYxJ8ELo%2FDmHinKlYpSM17lGMKBO4ls9rRvVYMgNSmTuvpPEVyRH0Kuk%2F1MxCHYYpO9SNb0I987plSo4qP%2FbvF3RSiq91yOh%2BhUwIzPrdRkLPPBW22UDAfY1danIN6xINOTcqjnTxPG3SSX86v1Y4SewomuGA542oid%2BoDLi29qmQZr%2FaAjzVxoAIEFgbWKjU8%2BF8zAJVZw4AaQyvuvYtiFUZkvOjCQgagZHLob51c0X3MIBsRmc0rmzyUo14eaHcZvwdjUNgvFKPc%2B0HLq%2FwyWJQWZRZFvAlqoQVMOLyb1%2BK0XCALV9MlcmfLs8gethgIhKgtxxkOLTSJ%2F93j2isbxZ9PXMLjbBcmyAAENJdQa%2Fg4qMnlWHHsg027jDD42JWrBjq0AlpvDMI0AtCKCFCBlR7xjStB53ajj27x36O2woPoaouILtAhGZRxuCDaCgREUWdhgj7GuHX0zOVO2qa4%2BIKjrZSKlg0cd90iC7pGghucUmL6vz236R2oidpn0n2pW2GIlrQK3nda1lSUyIkOZuXATOhhup9JHZZ%2FGfrbtuvo5Da4SYK3fRU9riUkJcQU6zuLrVWHfExPK45BioAjZkfkv5oBJPrs1Mv27Okz3IOiGqYs90odTEc%2FYa6psk6OE77DPW1ZtmqtK%2BCnF6Klbn3BCsan%2B9PwJJ2xeVWWZTtvlHGuChwsLWMPWfIzT%2FZGquRR6Dk2tjZbkuomYIctsohRfYtb%2FPJXXYYcCON7DrjFoLQNTAbKK422UqTcB3YUa6ooPXWDyne9Q%2BhbpARew9QItpZrZBp8&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20231128T050901Z&X-Amz-SignedHeaders=host&X-Amz-Expires=300&X-Amz-Credential=ASIA4FXKX5MD6P5UD5AN%2F20231128%2Feu-north-1%2Fs3%2Faws4_request&X-Amz-Signature=f14190b9abfda47899a2749684ef92e5731907c191b34e2282cd99495318d2b2"},
        {"id": 5, "name": "Coca-cola 1 литр", "quantity": 5, "price": 400,
         "image": "/media/photos/2023/11/23/thumb_page_4e299acc1d077cfaadc6d7053db94346.jpg"},
        {"id": 7, "name": "Картофель фри", "quantity": 0, "price": 500, "image": "https://bugbytes-django-s3-demo.s3.eu-north-1.amazonaws.com/photos/2023/11/27/aviko_frytki-original_750g.png?response-content-disposition=inline&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE4aCmV1LW5vcnRoLTEiRzBFAiBKBj3hLiS05xEJaqJJytYJWh749I26GlnELD5lA0UEVAIhAKl6UWl37tTA%2F9n768ZkUDGRE3GDXjQr%2FFhjJ1z46A%2FQKu0CCKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMODM2OTM3MTgxOTU5Igx7eU3a2UW9PtZmhAoqwQJwh2t%2F1%2Fbypb%2FWpyOhLBMSdkLPL94GRiVmC%2FsrRqbceVVMdpEUg9TKoM2ykxNlHzuaVQwxUcZDoI1Ud3NDCFOvNYn7eVWkcUZ28EJJK7IQcACB0RiZWzNTSCHcynT6IsI6TljaFPtoXiEOLH%2FXcOeHQ5q3iN8nerwkUoJOiUd9nemev0XeZ%2FAYtDAdpq1Vwq9RoaPO7VfzMsv%2BdttJzpLAkoncrVOSvzAJcS%2BSZnW7Qc6ByXyc49k5OaV%2FhERu9ObpFH1U4zDmE4GMIzwAXIakFuF9BcNNLmh4f%2FwlSRMTwXqVaZijKugbKdlnNHI4eIYoMPnMHFxYMyHbfonwvHnr9k4pPcbtXV47oawRuY0MLrX9L9xnfMIQyPyrB4ocNWOThADuuO%2B1TUppcGg8cemxyr6UPoqMvoVVNf6XrxxhqBYwnsuSqwY6swIXWUgbgZzAkLVqH2BgP8oO9nzkDV8gFdSz%2Bq%2BB3QjVqr7yXF%2FoRXyN1O%2BeCWNvyeTks%2Fgu%2F%2BdE9VEoF%2BBoIpss3rITZpz4w5FlWtm6SEfwrHr6%2FdkU06H%2F8ahkxrrUUlcOZ2Wih7hoKGD2s%2BqpwWZDx80QVHF0J9DBPFXGx3JiAN4%2BjyIqqBpSwRK%2B8WCqH8Mfrj2zlR9Y7Lt76rpPJnfMHipDVlcLTKVBzXd45Vtx%2F6zH6DSowFnsgFoVf8UsjaDW7b8ZtWKOa2GutiwI1K2VgmnYz6UEDBSd0kItt1McY1vRz5UE%2BPdDJKIGaiSNVFi0wAbqCsYWNKG7QTxAoC20Hjnyok55EGiJEYcz1ahT7RXDi5bscaWpVIP7S35jxBrs0R7Hp1ovFcrx3Nu0LveNst%2B7&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20231127T193606Z&X-Amz-SignedHeaders=host&X-Amz-Expires=300&X-Amz-Credential=ASIA4FXKX5MDQGE5RVO6%2F20231127%2Feu-north-1%2Fs3%2Faws4_request&X-Amz-Signature=8031c3ea9d26a023f7aedbd284d42b15e3ddb43d6640248166859b8f01cc51bd"},
        {"id": 8, "name": "Кепка", "quantity": 124, "price": 1500, "image": "https://bugbytes-django-s3-demo.s3.eu-north-1.amazonaws.com/photos/2023/11/27/%D0%BA%D0%B5%D0%BF%D0%BA%D0%B0.jpg?response-content-disposition=inline&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE4aCmV1LW5vcnRoLTEiRzBFAiBKBj3hLiS05xEJaqJJytYJWh749I26GlnELD5lA0UEVAIhAKl6UWl37tTA%2F9n768ZkUDGRE3GDXjQr%2FFhjJ1z46A%2FQKu0CCKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMODM2OTM3MTgxOTU5Igx7eU3a2UW9PtZmhAoqwQJwh2t%2F1%2Fbypb%2FWpyOhLBMSdkLPL94GRiVmC%2FsrRqbceVVMdpEUg9TKoM2ykxNlHzuaVQwxUcZDoI1Ud3NDCFOvNYn7eVWkcUZ28EJJK7IQcACB0RiZWzNTSCHcynT6IsI6TljaFPtoXiEOLH%2FXcOeHQ5q3iN8nerwkUoJOiUd9nemev0XeZ%2FAYtDAdpq1Vwq9RoaPO7VfzMsv%2BdttJzpLAkoncrVOSvzAJcS%2BSZnW7Qc6ByXyc49k5OaV%2FhERu9ObpFH1U4zDmE4GMIzwAXIakFuF9BcNNLmh4f%2FwlSRMTwXqVaZijKugbKdlnNHI4eIYoMPnMHFxYMyHbfonwvHnr9k4pPcbtXV47oawRuY0MLrX9L9xnfMIQyPyrB4ocNWOThADuuO%2B1TUppcGg8cemxyr6UPoqMvoVVNf6XrxxhqBYwnsuSqwY6swIXWUgbgZzAkLVqH2BgP8oO9nzkDV8gFdSz%2Bq%2BB3QjVqr7yXF%2FoRXyN1O%2BeCWNvyeTks%2Fgu%2F%2BdE9VEoF%2BBoIpss3rITZpz4w5FlWtm6SEfwrHr6%2FdkU06H%2F8ahkxrrUUlcOZ2Wih7hoKGD2s%2BqpwWZDx80QVHF0J9DBPFXGx3JiAN4%2BjyIqqBpSwRK%2B8WCqH8Mfrj2zlR9Y7Lt76rpPJnfMHipDVlcLTKVBzXd45Vtx%2F6zH6DSowFnsgFoVf8UsjaDW7b8ZtWKOa2GutiwI1K2VgmnYz6UEDBSd0kItt1McY1vRz5UE%2BPdDJKIGaiSNVFi0wAbqCsYWNKG7QTxAoC20Hjnyok55EGiJEYcz1ahT7RXDi5bscaWpVIP7S35jxBrs0R7Hp1ovFcrx3Nu0LveNst%2B7&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20231127T194607Z&X-Amz-SignedHeaders=host&X-Amz-Expires=300&X-Amz-Credential=ASIA4FXKX5MDQGE5RVO6%2F20231127%2Feu-north-1%2Fs3%2Faws4_request&X-Amz-Signature=52e491a1006233fe7767b723c9202d0222fc9a9ef3b9343715d9208bab89039c"},
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
        {"id": 7, "name": "Vintage pink dress", "quantity": 0, "price": 500,
         "image": "https://bugbytes-django-s3-demo.s3.eu-north-1.amazonaws.com/photos/2023/11/28/pink_dress.jpg"},
        {"id": 8, "name": "Кепка", "quantity": 124, "price": 1500, "image": "https://bugbytes-django-s3-demo.s3.eu-north-1.amazonaws.com/photos/2023/11/27/%D0%BA%D0%B5%D0%BF%D0%BA%D0%B0.jpg"},
    ]
    return render(request, "product.html", {"items": items})


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
