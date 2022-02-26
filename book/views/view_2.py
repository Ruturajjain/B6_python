from .importer import *


def view_c(request):
    return HttpResponse("in views c")

def view_d(request):
    return HttpResponse("in views d")