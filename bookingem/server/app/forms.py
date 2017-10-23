from django import forms
from .models import Category

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::

class GoodFiltersForm(forms.Form):
    category = forms.ModelChoiceField(queryset=Category.objects.all(),
            label='категория', empty_label=None)
    in_stock = forms.BooleanField(initial=True, label="В наличии", required=False)
    