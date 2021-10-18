from django import forms
from django.forms import ModelForm, TextInput, Textarea
from .models import Todos


class TodoForm(ModelForm):
    
    class Meta:
        model = Todos
        fields=['part','description','qty','vendor', 'rush','duedate','refnum','toapprove','tobill','billed','amount']
        # widgets = {
        #     'refnum': forms.TextInput(attrs={'placeholder': 'Stock, Work or Sales Order'}),
        #     'vendor': forms.Textarea(attrs={'cols': 180,'rows':20}),
        #     'description': forms.TextInput(attrs={'placeholder': 'Include Material, size and any other pertaining attribute'}),

        