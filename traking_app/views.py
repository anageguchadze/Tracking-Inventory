from django.shortcuts import render, redirect
from django import forms
from .models import Inventory


class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['name', 'serial_number', 'value']
        widgets = {
            'value': forms.NumberInput(attrs={'step': '0.01'})
        }

def index(request):
    if request.method == 'POST':
        form = InventoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = InventoryForm()

    inventories = Inventory.objects.all()
    return render(request, 'index.html', {'form': form, 'inventories': inventories})
