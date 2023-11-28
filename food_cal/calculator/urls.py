from django.urls import path
from . import views
urlpatterns=[
    path("", views.add,name = "cal"),
    path("check", views.check,name = "check"),
    path("food", views.lookup,name = "food"),
    path("nutrition", views.lookup,name = "nutrition"),
]