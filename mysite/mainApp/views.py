from django.shortcuts import render


def index(request):
    return render(request, 'mainApp/homePage.html')


def contact(request):
    return render(request, 'mainApp/basic.html', {'values': ['Якщо залишились питання, то дзвоніть за номером',
                                                             '(066) 44 86 166', 'example.gmail.com']})
# Create your views here.
