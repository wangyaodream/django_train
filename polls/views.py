from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(r):
    return HttpResponse("Hello,World! this is polls app index.")

