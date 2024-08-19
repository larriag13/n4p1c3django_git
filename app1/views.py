from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("<h1>Soy el index de app1</h1>")

def vista1(request):
    html="""
    <h1 style="color:red">Soy un título de app1</h1>
    <h2>Soy un subtítulo de app1</h2>
    """
    return HttpResponse(html)
