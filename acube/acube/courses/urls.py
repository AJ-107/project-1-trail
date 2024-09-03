from django.urls import path
from.import views

urlpatterns = [
    path("web/", views.web, name="web development"),
    path("pyt/", views.pyt, name="python"),
    path("datasci/", views.datasci, name="data science"),
]
