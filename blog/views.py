from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.shortcuts import redirect


# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'  # Instead of object_list
    login_url = '/login/'


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


class RegisterView(FormView):
    template_name = 'blog/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)
