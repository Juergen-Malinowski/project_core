from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

fruits = [
    {"name": "Apfel", "weight": 150, "color": "rot"},
    {"name": "Banane", "weight": 220, "color": "gelb"},
    {"name": "Orange", "weight": 190, "color": "orange"},
    {"name": "Kiwi", "weight": 70, "color": "grün"},
    {"name": "Birne", "weight": 180, "color": "grün"}    
]


def start_page_view(request):
    return HttpResponse('START-Seite !!!!!!!!!')

# def fruit_view(request):
#    return HttpResponse('FRUIT-Seite wurde aufgeruten !!!!!!!!!!')

def send_fruit(request):
    return JsonResponse({"fruits": fruits})
    # ALTERNATIVE (aber schalten Django-Sicherung ab) ...
    # return JsonResponse(fruits, safe=False)
