from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, CreateView, UpdateView, DetailView

from blog.forms import BlogCreateForm
from blog.models import Blog


# Create your views here.
class BlogListView(ListView):
    model = Blog
    template_name = 'blog/blog_list.html'


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog/blog_detail.html'

    def get_object(self, queryset=None):
        objects = super().get_object()
        objects.view += 1
        objects.save()
        return objects


class BlogCreateView(CreateView):
    model = Blog
    template_name = 'blog/blog_create.html'
    success_url = reverse_lazy('blog:list')
    form_class = BlogCreateForm

    def form_valid(self, form):
        self.object = form.save()
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)


class BlogUpdateView(UpdateView):
    model = Blog
    template_name = 'blog/blog_create.html'
    success_url = reverse_lazy('blog:list')
    form_class = BlogCreateForm


class BlogDeleteView(DeleteView):
    model = Blog
    template_name = 'blog/blog_delete.html'
    success_url = reverse_lazy('blog:list')
