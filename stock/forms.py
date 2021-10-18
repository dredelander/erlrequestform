from django import forms
from django.forms import ModelForm, TextInput, Textarea
from .models import StockOut


class StockOutForm(ModelForm):
    
    class Meta:
        model = StockOut
        fields=['part','qty_onHand','qty_onSystem','impact','orders', 'recurring','on_order','duedate','vendor','late','po_number','reazon', 'other']