from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Post
from .forms import PostForm, CommentForm
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login



### Registration

class RegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = 'user/login/'
    template_name = 'partial/register.html'

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)

### Login

class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = "account/login.html"
    success_url = "/"

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


### Homepage

def home(request):
    postList = Post.objects.filter(visible='1')
    paginator = Paginator(postList, 6)
    page = request.GET.get('page')
    querysetGoods = paginator.get_page(page)

    context = {
        "posts": postList,
        "title": "Homepage",
        "desc": "Decription",
        "key": "keys",
    }
    return render(request, "partial/home.html", context)


### Article
def single(request, id=None):
    post = get_object_or_404(Post, id=id)

    context = {
        "post": post,
    }
    return render(request, "partial/single.html", context)


### Post create

def postCreate(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = PostForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.user = request.user
                post.created = timezone.localtime()
                post.save()
                return redirect('single', id=post.pk)
        else:
            form = PostForm()
        return render(request, 'partial/post_create.html', context={'form': form})
    else:
        return redirect('login')
"""
### Post edit

def PostEdit(request, id):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, id=id)
        if request.method == "POST":
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.user = request.user
                post.created = timezone.localtime()
                post.save()
                return redirect('single', id=post.pk)
        else:
            form = PostForm(instance=post)
        return render(request, 'partial/post_create.html', {'form': form})
    else:
        return redirect('single', id=Post.pk)
"""
### Comments

def AddComment(request, id):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, id=id)
        if request.method == "POST":
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.post = post
                comment.save()
                return redirect('single', id=post.pk)
        else:
            form = CommentForm()
        return render(request, 'partial/add_comment.html', {'form': form})
    else:
        return redirect('login')

