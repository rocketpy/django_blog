from django.shortcuts import render


def post_list(request):
    return render(request, 'blog_app/posts_list.html', {})

