from .models import Post
from django.shortcuts import render
from django.utils import timezone
from django.views import generic
from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets 
from .model import Language
from .serializers import LanguageSerializer


class LanguageView(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})



"""
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'
"""
