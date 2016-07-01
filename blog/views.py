from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.views.decorators.http import require_http_methods
from django.core.urlresolvers import reverse

from .models import Post, User
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
    user = User.objects.all()[0]
    post = Post(author=user)
    form = PostForm(request.POST, instance=post)
    post = form.save()
    return HttpResponseRedirect(reverse('index'))


def view(request, post_id):
    post = Post.objects.get(id=post_id)
    template = loader.get_template('post/view.html')
    context = RequestContext(request, {
        'post': post
    })
    return HttpResponse(template.render(context))