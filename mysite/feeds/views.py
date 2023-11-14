from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from feeds.models import Articles
from feeds.forms import ArticlesForm
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def post_list(request):
    posts = Articles.objects.all()
    user = Articles.user
    paginator = Paginator(posts, 3)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {
        'title': 'News list',
        'object_list': posts,
        'page_request_var': page_request_var,
        'user': user,

    }
    return render(request, 'feeds/post_list.html', context)


def post_create(request):
    form = ArticlesForm(request.POST or None, request.FILES or None)
    if not request.user.is_staff:
        raise render(request, 'User is not registered', status=404)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Post created!!!")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        'title': 'Post create',
        'form': form
    }
    return render(request, 'feeds/post_create.html', context)


def post_update(request, id):
    instance = get_object_or_404(Articles, id=id)
    form = ArticlesForm(request.POST or None,
                        request.FILES or None,
                        instance=instance)
    if not request.user.is_staff:
        raise render(request, '404.html', status=404)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "<a href = '#'>Post updated!!!</a> ", extra_tags='safe_html')
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        'title': 'Post update',
        'form': form
    }

    return render(request, 'feeds/post_create.html', context)


def post_delete(request, id):
    instance = get_object_or_404(Articles, id=id)
    instance.delete()
    messages.success(request, "Post deleted!!!")
    if not request.user.is_staff:
        raise render(request, '404.html', status=404)
    return redirect('feeds:post_list')


def post_detail(request, id):
    instance = get_object_or_404(Articles, id=id)
    context = {
        'title': 'Post detail',
        'object': instance
    }
    if not request.user.is_staff:
        raise render(request, '404.html', status=404)
    return render(request, 'feeds/post_detail.html', context)
