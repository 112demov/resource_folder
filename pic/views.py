from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .models import Picture
from django.shortcuts import render
from django.urls import reverse_lazy



class PicListView(ListView):
    paginate_by = 16
    model = Picture
    template_name = 'pic/pic.html'
    
class PicDetailView(DetailView):
    model = Picture
    template_name = 'pic/foto.html'
        
class PicCreateView(CreateView):
    model = Picture
    template_name = 'pic/add.html'
    fields = ['img', 'title', 'alt']
    
class PicDeleteView(DeleteView):
    model = Picture
    template_name = 'pic/delete.html'
    success_url = reverse_lazy('pic')

