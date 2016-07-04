from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.views.decorators.http import require_http_methods
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db import IntegrityError

from .models import Post
from .forms import PostForm

def index(request):
    posts = Post.objects.order_by('-created_at')
    template = loader.get_template('post/index.html')
    form = PostForm()
    context = RequestContext(request, {
        'posts': posts,
        'form': form
    })
    return HttpResponse(template.render(context))

@require_http_methods(["POST"])
def add_post(request):
    if request.user.is_authenticated():
        post = Post(author=request.user)
        form = PostForm(request.POST, instance=post)
        post = form.save()
    else:
        messages.error(request, 'You must be authenticate to add post')
    return HttpResponseRedirect(reverse('index'))


def view(request, post_id):
    post = Post.objects.get(id=post_id)
    template = loader.get_template('post/view.html')
    context = RequestContext(request, {
        'post': post
    })
    return HttpResponse(template.render(context))

@require_http_methods(["POST"])
def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
        else:
            messages.error(request, 'Your account is disabled :(')
    else:
        messages.error(request, 'Invalid username or password')
    return HttpResponseRedirect(reverse('index'))

@require_http_methods(["POST"])
def register_view(request):
    try:
        user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
    except IntegrityError, e:
        messages.error(request, 'User cannot be created, reason: ' + str(e))
    return HttpResponseRedirect(reverse('index'))

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))