from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
    return render(request, 'hello.html')

def action_page(request):
    username = request.POST.get('uname')
    pw = request.POST.get('psw')

    return render(request, 'action_page.html',{'pw':pw})
