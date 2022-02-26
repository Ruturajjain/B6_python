from .importer import *

def view_a(request):
    return HttpResponse("in views a")

def view_b(request):
    return HttpResponse("in views b")