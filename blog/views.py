from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.cache import cache
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, CreateView, UpdateView, DetailView

from blog.forms import BlogCreateForm
from blog.models import Blog


# Create your views here.
class BlogListView(LoginRequiredMixin, ListView):
    model = Blog
    template_name = 'blog/blog_list.html'


class BlogDetailView(LoginRequiredMixin, DetailView):
    model = Blog
    template_name = 'blog/blog_detail.html'

    def get_object(self, queryset=None):
        objects = super().get_object()
        objects.view += 1
        objects.save()
        return objects

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        if settings.CACHE_ENABLED:
            key = 'context_data'
            data_list = cache.get(key)
            if data_list is None:
                data_list = Blog.objects.all()
                cache.set(key, data_list)
        else:
            data_list = Blog.objects.all()
        context_data['objects'] = data_list
        return context_data


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    template_name = 'blog/blog_create.html'
    success_url = reverse_lazy('blog:list')
    form_class = BlogCreateForm

    def form_valid(self, form):
        self.object = form.save()
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Blog
    template_name = 'blog/blog_create.html'
    success_url = reverse_lazy('blog:list')
    form_class = BlogCreateForm


class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Blog
    template_name = 'blog/blog_delete.html'
    success_url = reverse_lazy('blog:list')
