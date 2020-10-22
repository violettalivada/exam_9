from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.models import Image
from webapp.mixins import CustomMixin


class IndexView(ListView):
    template_name = 'images/index.html'
    context_object_name = 'images'
    model = Image
    ordering = '-created_at'


class ImageDetailView(DetailView):
    template_name = 'images/detail.html'
    pk_url_kwarg = 'pk'
    model = Image


class ImageCreateView(CustomMixin, CreateView):
    template_name = 'images/create.html'
    model = Image
    fields = ['image', 'description']

    def form_valid(self, form):
        form.instance.author_name = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('webapp:index')


class ImageUpdateView(UpdateView):
    model = Image
    template_name = 'images/update.html'
    fields = ['image', 'description', 'author']
    context_object_name = 'obj'

    def get_success_url(self):
        return reverse('webapp:product_view', kwargs={'pk': self.object.pk})


class ImageDeleteView(DeleteView):
    template_name = 'images/delete.html'
    model = Image
    context_object_name = 'image'
    success_url = reverse_lazy('webapp:index')
