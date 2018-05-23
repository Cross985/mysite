from django.shortcuts import render
from django.views import generic
from .models import Item
from django.template import loader

# Create your views here.
class IndexView(generic.ListView):
    # Display all Items in DB
    template_name = 'Item/index.html'
    context_object_name = 'item_list'
    model = Item

    def get_queryset(self):
        return Item.objects.all()

