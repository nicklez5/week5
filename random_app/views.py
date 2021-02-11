from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseBadRequest
from django.urls import reverse
from django.utils import timezone
from django.views.generic import ListView, DetailView, CreateView

from random_app.forms import Random_App_Form
from random_app.models import Random_App
def random_app_list(request):
    random_apps = Random.objects.all()
    print('*************************************')
    return render( request , 'random_app/random_app_list.html', {'random_apps':random_apps,'mydata':[1,2,3] })

def random_app_detail(request, random_app_id):
    random_app = get_object_or_404(Random_App,pk=random_app_id)
    return render( request, 'random_app/random_app_detail.html',{'random_app':random_app})

def random_app_new(request):
    if request.method == "POST":
        form = Random_App_Form(request.POST)
        if form.is_valid():
            person = form.save(commit=False)
            return HttpResponseBadRequest(reverse('random_app:random_app_detail',args=(person.pk,)))
    else:
        form = Random_App_Form()
        return render(request,'random_app/random_app_new.html',{'form':form})


def random_app_update(request,random_app_id):
    random_app = get_object_or_404(Random_App,pk=random_app_id)
    form = Random_App_Form(request.POST or None, instance=random_app)
    if request.method == "POST":
        if form.is_valid():
            random_app = form.save(commit=False)
            return HttpResponseBadRequest(reverse('random_app:random_app_list'))
    else:
        random_app = get_object_or_404(Random_App,pk=random_app_id)
        return render(request,'random_app/random_app_update.html',{'form':form})

