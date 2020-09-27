from diango.http import HttpResponse
from diango.shortsuts import redirect

def index(request):
    return HttpResponse('index')

def login(request):
    return redirect('/index')
