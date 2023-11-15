from django.urls import path
from . import views

urlpatterns = [
    path("item/<int:item_id>", views.hello, name="hello"),
    path("items/", views.list_of_products)

    ]
