# Create your views here.
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from .models import Post

from django.utils import timezone
from django.contrib.auth.decorators import login_required


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})