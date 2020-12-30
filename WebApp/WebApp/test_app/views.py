from django.shortcuts import render
from django.http import HttpResponse
from .models import TestClass
from .serializers import TestSerializer
import os
# Create your views here.


def init_counter(request):
    t = TestClass()
    t.save()
    ret = "<html><body>First: " + str(t.counter1) + " Second: " + str(t.counter2) + "</body></html>"
    return HttpResponse(content=ret, status = 200)


def test_route(request):
    ret = "<html></html>"

    ver = os.environ.get("VER")

    if int(ver) == 1:
        try:
            t = TestClass.objects.get(id=1)
            t.counter1 += 1
            t.save()
            ret = "<html><body>First: " + str(t.counter1) + "</body></html>"
        except TestClass.DoesNotExist:
            return HttpResponse(status=404)
    elif int(ver) == 2:
        try:
            t = TestClass.objects.get(id=1)
            t.counter2 += 1
            t.save()
            ret = "<html><body>Second: " + str(t.counter1) + "</body></html>"
        except TestClass.DoesNotExist:
            return HttpResponse(status=404)
    return HttpResponse(content=ret, status=200)

