from django.urls import path
from .views import *

urlpatterns = [
    path("", list_orders),
    path("display", display_order),
    path("create/", create_order),
    path("update", update_order),
    path("delete", delete_order)
]
