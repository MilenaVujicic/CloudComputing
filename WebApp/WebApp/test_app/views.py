from django.shortcuts import render
from.models import TestClass
from django.http import HttpResponse
# Create your views here.


def test_route(request):
    return HttpResponse(content="Hello World", status=200)