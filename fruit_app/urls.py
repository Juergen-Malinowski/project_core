from django.urls import path
from .views import send_fruit

urlpatterns=[
    path('', send_fruit),
]