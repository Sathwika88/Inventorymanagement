from django import forms  
from myapp.models import warehouse
class WarehouseForm(forms.ModelForm):  
    class Meta:  
        model = warehouse 
        fields = ['brand_no', 'brand_name', 'size','quantity_boxes','quantity_bottles'] 
        widgets = { 'brand_no': forms.TextInput(attrs={ 'class': 'form-control' }), 
            'brand_name': forms.TextInput(attrs={ 'class': 'form-control' }),
            'size': forms.TextInput(attrs={ 'class': 'form-control' }),
            'quantity_boxes': forms.TextInput(attrs={ 'class': 'form-control' }),
            'quantity_bottles': forms.TextInput(attrs={ 'class': 'form-control' }),
            
      }