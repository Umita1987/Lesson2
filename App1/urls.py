from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path("item/<int:item_id>", views.hello, name="hello"),
    path("items/", views.list_of_products, name="products"),
    path("", views.main_page, name="main"),
    path("about/", views.about, name="about"),
    path("fill/", views.fill, name="fill"),
    path("create/", views.create_item, name="create"),
    path("read/<int:item_id>", views.read_item, name="get"),
    path("update/<int:item_id>", views.update_item, name="update"),
    path("delete/<int:item_id>", views.delete_item, name="delete"),
    path("upload/", views.image_upload_view, name="image")
    ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
