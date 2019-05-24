from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import *


def index(request):
    return HttpResponse('Strona z klientami')