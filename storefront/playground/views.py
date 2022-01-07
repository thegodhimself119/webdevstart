from django.shortcuts import render
from django.http import HttpResponse
from . import  database
from pymongo import MongoClient
import certifi
from . import views


ca = certifi.where()
client = MongoClient("mongodb+srv://yubik:12345@cluster0.cklcq.mongodb.net/?retryWrites=true&w=majority", tlsCAFile=ca)
db = client["database"]#acess of current databaser
collist = db.list_collection_names()#finding collection list
login = bool()

# Create your views here.
def hello(request):
    return render(request, 'hello.html')

def action_page(request):
    username = request.POST.get('uname')
    pw = request.POST.get('psw')
    if username in collist:
        col = db[username]
        find = col.find({})
        for find in find:
            pw = find["password"]
        if pw == pw:
            return render(request, 'action_page.html', {'pw': pw})

    else:
        return render(request, 'notlign.html')





