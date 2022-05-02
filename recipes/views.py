from django.shortcuts import render

from .forms import recipesForm
from .models import recipesModel


def create_view(request):
    context = {}

    form = recipesForm(request.POST or None)
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, "create_view.html", context)
