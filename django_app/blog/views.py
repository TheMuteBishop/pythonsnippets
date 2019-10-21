from django.shortcuts import render,  get_object_or_404
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import (
        ListView,
        DetailView,
        CreateView,
        UpdateView,
        DeleteView
        )
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Post, Comment

def index(request):
    context = {
        "posts": Post.objects.all()
    }
    return render(request, 'blog/blog_home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/blog_home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 4


home = PostListView.as_view()

def about(request):
    return render(request, 'blog/blog_about.html',{})

def layout(request):
    return render(request, 'container.html',{"num_cards": [1,2,3,4,5]})

def mainpage(request):
    return render(request, 'landing.html',{"num_cards": [1,2,3,4,5]})

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs) 
        context['comments'] = Comment.objects.for_post(post=context['post'])
        print(context['comments'])
        return context


class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = [ 'title', 'content' ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = [ 'title', 'content' ]

    def form_valid( self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False



class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('blog:blog-home')

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_post.html'
    context_object_name = 'posts'
    paginate_by = 4

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

        
detail = PostDetailView.as_view()
create = PostCreateView.as_view()
update = PostUpdateView.as_view()
delete = PostDeleteView.as_view()
user_post = UserPostListView.as_view()
