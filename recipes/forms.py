from django import forms

from .models import recipesModel


class recipesForm (forms.ModelForm):
    class Meta:
        model = recipesModel

        fields = [
            "title",
            "description",

        ]
