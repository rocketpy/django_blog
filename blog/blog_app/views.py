from django.shortcuts import render
from django.utils import timezone
from .models import Post


def post_list(request):
    return render(request, 'blog_app/posts_list.html', {})

