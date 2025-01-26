from django.urls import path

from catalog import views

urlpatterns = [
    path("", views.index, name="index"),
    path("contacts/", views.contacts, name="contacts")
]