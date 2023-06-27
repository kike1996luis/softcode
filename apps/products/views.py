from django.views.generic import ListView, DetailView, CreateView 
from .models import Producto 
from .forms import ProductoForm

class ProductoListView(ListView): 
    model = Producto 
    template_name = 'producto_list.html' 
    context_object_name = 'productos'

class ProductoDetailView(DetailView): 
    model = Producto 
    template_name = 'producto_detail.html' 
    context_object_name = 'producto'

class ProductoCreateView(CreateView): 
    model = Producto 
    form_class = ProductoForm 
    template_name = 'producto_form.html'
    success_url = '/'