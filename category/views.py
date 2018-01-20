from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from category.models import Category


class CategoryList(ListView):
    model = Category


class CategoryCreate(CreateView):
    model = Category
    fields = ['name']
    success_url = reverse_lazy('category:category_list')


class CategoryUpdate(UpdateView):
    model = Category
    fields = ['name']
    success_url = reverse_lazy('category:category_list')


class CategoryDelete(DeleteView):
    model = Category
    success_url = reverse_lazy('category:category_list')