import django_filters
from django_filters import (
    CharFilter, 
    BooleanFilter,
    ChoiceFilter,
    ModelChoiceFilter, 

)
from django_filters.widgets import (
    BooleanWidget,
)
from django import forms
from .models import Product

from .models import *

class ProductFilter(django_filters.FilterSet):
    # name = CharFilter(field_name='name', lookup_expr='icontains',
    #                     widget=forms.TextInput(attrs={
    #                         'class':'blue'
    #                     }))
   
    brand = ChoiceFilter(choices=(("Celine", "Celine"),
                                    
                            ),
                            widget=forms.Select(attrs={
                                'class': 'mdb-select md-form'
                            }),
                            label='')
    # sort = ModelChoiceFilter(queryset=Product.objects.all())
    shoe = ChoiceFilter(widget=forms.RadioSelect, 
                    choices=(("Shoe", "Shoe"),)
                    )
    # featured = BooleanFilter(field_name='featured', widget=BooleanWidget())

    class Meta: 
        model = Product
        fields = ['brand']