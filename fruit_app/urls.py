from django.urls import path
from .views import fruit_view

urlpatterns=[
    path('', fruit_view)
]