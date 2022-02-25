from cgitb import html
from django.shortcuts import redirect, render
from django.http import HttpResponse
from . import database
from pymongo import MongoClient
import certifi
from . import views

ca = certifi.where()
client = MongoClient("mongodb+srv://yubik:12345@cluster0.cklcq.mongodb.net/?retryWrites=true&w=majority", tlsCAFile=ca)
db = client["database"]  # acess of current databaser
collist = db.list_collection_names()  # finding collection list
login = bool()


# Create your views here.
def hello(request):
    return render(request, 'hello.html')


def action_page(request):
    username = request.POST.get('logemail')
    pw = request.POST.get('logpw')
    x = "wrong username or password"
    if username in collist:
        col = db[username]
        find = col.find({})
        for find in find:
            y = find["password"]

        if pw == y:
            return redirect("/")

        else:
            return render(request, 'test.html', {'message': x})

    else:

        return render(request, 'test.html', {'message': x})


def register(request):
    username = request.POST.get('name')
    pw = request.POST.get('password1')
    pw2 = request.POST.get('password2')


def test(request):
    if request.method == 'POST':
        username = request.POST.get('logemail')
        pw = request.POST.get('logpw')
        x = "wrong username or password"
        if username in collist:
            col = db[username]
            find = col.find({})
            for find in find:
                y = find["password"]

            if pw == y:
                return redirect("/")

            else:
                return render(request, 'test.html', {'message': x})


        else:
            return render(request, 'test.html', {'message': x})

    else:
        return render(request, 'test.html')


def index(request):
    return render(request, 'index.html')


def newtest(request):
    return render(request, 'newtest.html')
