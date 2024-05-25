from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
# Create your views here.

about_=  {"name": "Алексей",
        "lastname" : "Букуев",
        "surname" : "Михайлович",
        "tel":"8-923-000-00-00",
        "email_":"abukuev@list.ru"
        }

items = [
{"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
{"id": 2, "name": "Куртка кожаная" ,"quantity":2},
{"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
{"id": 7, "name": "Картофель фри" ,"quantity":0},
{"id": 8, "name": "Кепка" ,"quantity":124},
]

def home(request):
    context = {
        "name":"Букуев Алексей Михайлович",
        "email":"abukuev@list.ru",
    }
    return render(request,'index.html',context)

def about(request):
    context = {
        'about_':about_
    }
    text= f"""
    Имя: {about_['name']}<br>
    Отчество: {about_['surname']}<br>
    Фамилия: {about_['lastname']}<br>
    телефон: {about_['tel']}<br>
    email: {about_['email_']},
    """
    return render(request,'about.html',context)

def get_items(request):
    context={
        'items':items
    }
    
    return render(request,'items.html',context)

def get_item(request,item_id):

    context={
        'items':items,
        'item_id':item_id
    }
    return render(request,'item.html',context)

'''
    for item in items:
        if item['id'] == item_id:
            context = {
                "item":item
            }
            return render(request,'item.html',context)
    return HttpResponseNotFound(f"{item_id} Not Found")
    '''