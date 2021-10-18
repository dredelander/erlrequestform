from django import forms
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class StockOut(models.Model):

    EFFECT_CHOICES=(
        ("1", "Stock out has stopped production")
        ("2", "Stock out prevented an order to ship")
        ("3", "Low stock warning, no sales impact, review System parameters")
        ("4", "Need to adjust inventory, review BOMS")
    )

    SUPPLY_CHOICES=(
        ("1", "Inventory was off prior new order")
        ("2", "Vendor is past due, LATE w/o update")
        ("3", "Covid Related Issues on vendor side")
        ("4", "Staffing Issues on vendor side")
        ("5", "Order update/change by ERL")
        ("6", "Sales Order did not account for actual component's lead-time")
        ("7", "Delay due to transit/shipping issue")
    )

    part = models.CharField(max_length=50)
    qty_onHand = models.IntegerField()
    qty_onSystem = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    impact = forms.ChoiceField(choices = EFFECT_CHOICES)
    orders = models.TextField(max_length=250)
    recurring = models.BooleanField(default=False)

    on_order = models.BooleanField(default=False)
    duedate = models.DateField()
    vendor = models.CharField(max_length=50)
    late= models.BooleanField(default=False)
    po_number = models.CharField(max_length=11)
    reazon =  forms.ChoiceField(choices = SUPPLY_CHOICES)
    other = models.TextField(max_length=250)
    datecompleted = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.part