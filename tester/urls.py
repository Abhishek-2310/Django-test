from django.urls import path
from . import views
app_name = "tester"

urlpatterns = [
    path("", views.simple_view, name="simple_view"),
]
