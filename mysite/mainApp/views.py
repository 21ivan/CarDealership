from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from .models import Car

# Create your views here.


def index(request):
    return render(request, 'mainApp/homePage.html')


def cars_list(request):
    queryset = Car.objects.all()
    paginator = Paginator(queryset, 3)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)
    context = {
        'title': 'Cars list',
        'queryset': queryset,
        'page_request_var': page_request_var,
    }
    return render(request, 'mainApp/cars_list.html', context)