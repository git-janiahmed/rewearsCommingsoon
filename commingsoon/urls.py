from django.urls import path, include
from .views import CommingSoonRegister, CommingSoonSucess

urlpatterns = [
    path("", CommingSoonRegister.as_view(), name="commingIndex"),
    path("sucess", CommingSoonSucess.as_view(), name="commingSucess"),
]
