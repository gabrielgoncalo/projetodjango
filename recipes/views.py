from multiprocessing import context
from django.shortcuts import render
from django.urls import path
from .forms import recipesForm
from .models import recipesModel
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)


def create_view(request):
    context = {}

    form = recipesForm(request.POST or None)
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, "create_view.html", context)


def list_view(request):
    context = {}


    context["dataset"] = recipesModel.objects.all()
    return render(request,"list_view.html", context)


def detail_view(request, id):
    context = {}

    context["data"] = recipesModel.objects.get(id = id)
    return render(request, "detail_view.html", context)

def update_view(request, id):
    context = {}

    obj = get_object_or_404(recipesModel, id = id)
    form = recipesForm(request.POST or None, instance = obj)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/"+id)

    context["form"] = form
    return render(request, "update_view.html", context)

def delete_view(request, id):
    context = {}

    obj = get_object_or_404(recipesModel, id = id)
    

    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/")

    
    return render(request, "delete_view.html", context)



