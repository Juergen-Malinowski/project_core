from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def start_page_view(request):
    return HttpResponse('START-Seite !!!!!!!!!')

def fruit_view(request):
    return HttpResponse('FRUIT-Seite wurde aufgeruten !!!!!!!!!!')
