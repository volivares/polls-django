from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, World. Yout're at the polls index.")
