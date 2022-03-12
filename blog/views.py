from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

#created for detail views of post, url in urls.py /post/1/ (i.e.)
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', { 'posts': posts })
