from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Page
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import PageForm
# Create your views here.


#DEVOLVER UNA LISTA DE LAS INSTANCIAS DE UN MODELO
#ListView
class PageListView(ListView):
    model = Page
    
#DEVOLVER UNA INSTANCIA DE UN MODELO
#DetailView
class PageDetailView(DetailView):
    model = Page
    
class PageCreateView(CreateView):
    model = Page
    form_class = PageForm
    success_url = reverse_lazy('pages:pages')
    
class PageUpdateView(UpdateView):
    model = Page
    form_class = PageForm
    template_name_suffix = "_update_form"
    def get_success_url(self):
        return reverse_lazy('pages:update', args=[self.object.id]) + "?ok"

class PageDeleteView(DeleteView):
    model = Page
    success_url = reverse_lazy("pages:pages")