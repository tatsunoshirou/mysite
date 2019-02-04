from django.shortcuts import render, redirect

# Create your views here.
from django.http.response import HttpResponseRedirect
from django.template.response import TemplateResponse
from django.http import Http404
from django.urls import reverse
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from polls.models import Post
from polls.forms import PostForm


def post_list(request):
    posts = Post.objects.order_by('-created_at')

    paginator = Paginator(posts, 9)

    page = request.GET.get('page', 1)
    posts = paginator.page(page)

    return TemplateResponse(request, 'polls/post_list.html',
                            {'posts': posts})


def post_detail(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        raise Http404
    return TemplateResponse(request, 'polls/post_detail.html',
                            {'post': post})


@login_required()
def index(request):
    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('post_list'))
    else:
        form = PostForm()
    posts = Post.objects.order_by('-created_at')
    context = {'posts': posts, 'form': form}

    return TemplateResponse(request, 'polls/index.html', context)
