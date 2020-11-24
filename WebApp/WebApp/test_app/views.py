from django.shortcuts import render
from.models import TestClass
from django.http import HttpResponse
from .models import TestClass
from .serializers import TestSerializer
# Create your views here.


def init_counter(request):
    t = TestClass()
    serializer = TestSerializer(t)
    if serializer.isValid():
        serializer.save()

    return HttpResponse(status=
                        200)


def test_route(request):
    try:
        t = TestClass.objects.get(id=1)
        t.counter += 1
        t.save()
    except TestClass.DoesNotExist:
        return HttpResponse(status=404)

    return HttpResponse(content=t.counter, status=200)

