from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import *


def index(request):
    posts = Sportnews.objects.all()

    return render(request, 'blok/index.html', {'posts': posts})


def about(request):
    return render(request, 'blok/about.html')


def detail(request, sportnews_id):
    a = Sportnews.objects.get(id=sportnews_id)

    comment_list = a.comment_set.order_by('-id')[:10]
    return render(request, 'blok/detail.html', {'bloks': a, 'comment_list': comment_list})


def l_comment(request, sportnews_id):
    try:
        a = Sportnews.objects.get(id=sportnews_id)
    except:
        raise Http404('Статья не найдено')

    a.comment_set.create(user=request.POST['name'], comments=request.POST['text'])
    return HttpResponseRedirect(reverse('blok:detail', args=(a.id,)))
