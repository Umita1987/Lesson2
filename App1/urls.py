from django.urls import path
from . import views

urlpatterns = [
    path("item/<int:item_id>", views.hello, name="hello"),
    path("items/", views.list_of_products),
    path("", views.main_page),
    path("about/", views.about),
    path("fill/", views.fill, name="fill"),
    path("create/", views.create_item, name="create"),
    path("read/<int:item_id>", views.read_item, name="get"),
    path("update/<int:item_id>", views.update_item, name="update"),
    path("delete/<int:item_id>", views.delete_item, name="delete")

    ]
