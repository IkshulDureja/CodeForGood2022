from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic, Webpage, AccessRecord

# Create your views here.


def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list}
    #my_dict={'insert_me':"Hello Now I am from views.py!"}
    return render(request, 'first_app/index.html', context=date_dict)


def breakfast(request):
    return render(request, 'first_app/breakfast.html')


def rescue(request):
    return render(request, 'first_app/rescue.html')


def ngo(request):
    return render(request, 'first_app/ngo.html')


def relief(request):
    return render(request, 'first_app/relief.html')
