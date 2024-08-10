from typing import Any
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post


def news(request):
    context = {
        'posts': Post.objects.all(),
        'title': 'News'
    }
    return render(request, 'news/news_page.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'news/news_page.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 6

class UserPostListView(ListView):
    model = Post
    template_name = 'news/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 6

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')



class PostDetailView(DetailView):
    model = Post

@method_decorator(staff_member_required, name='dispatch')
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title','status','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


@method_decorator(staff_member_required, name='dispatch')
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'status', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

@method_decorator(staff_member_required, name='dispatch')
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
