from django.shortcuts import render
from django.views.generic import ListView,CreateView,DetailView
from core.models import product


class productListView(ListView):
    model = product
    template_name = "index.html"


class ProductCreateView(CreateView):
    model = product
    fields =['name','Price','Description']
    template_name = "add.html"


class ProductDetailView(DetailView):
    model = product
    template_name = "product_details.html"



