from django.http import HttpResponse

def index(request):
    return HttpResponse("hello world, you are the poll index")
