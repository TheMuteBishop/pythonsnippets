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

from .models import Post

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

    # def get_context_data(self, **kwargs):
    #     context = super(PostListView, self).get_context_data(**kwargs) 
    #     context['top_posts'] = Post.objects.top_posts()
    #     return context

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
        context['top_posts'] = Post.objects.top_posts()
        return context


class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = [ 'title', 'content' ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # def get_context_data(self, **kwargs):
    #     context = super(PostCreateView, self).get_context_data(**kwargs) 
    #     context['top_posts'] = Post.objects.top_posts()
    #     print(context)
    #     return context

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

    # def get_context_data(self, **kwargs):
    #     context = super(PostUpdateView, self).get_context_data(**kwargs) 
    #     context['top_posts'] = Post.objects.top_posts()
    #     print(context)
    #     return context


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('blog:blog-home')

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    # def get_context_data(self, **kwargs):
    #     context = super(PostDeleteView, self).get_context_data(**kwargs) 
    #     context['top_posts'] = Post.objects.top_posts()
    #     print(context)
    #     return context

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

# ['__bytes__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_charset', '_closable_objects', '_container', '_content_type_for_repr', '_convert_to_charset', '_handler_class', '_headers', '_is_rendered', '_post_render_callbacks', '_reason_phrase', '_request', 'add_post_render_callback', 'charset', 'close', 'closed', 'content', 'context_data', 'cookies', 'delete_cookie', 'flush', 'get', 'getvalue', 'has_header', 'is_rendered', 'items', 'make_bytes', 'readable', 'reason_phrase', 'render', 'rendered_content', 'rendering_attrs', 'resolve_context', 'resolve_template', 'seekable', 'serialize', 'serialize_headers', 'set_cookie', 'set_signed_cookie', 'setdefault', 'status_code', 'streaming', 'tell', 'template_name', 'using', 'writable', 'write', 'writelines']