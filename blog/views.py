from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Blog, BlogComment
from .forms import CommentForm


def blog_list(request):
    blogs = Blog.objects.order_by('-id')
    context = {'blogs': blogs}
    return render(request, "blog/blog_list.html", context)


def blog_detail(request, pk):
    blog = get_object_or_404(Blog, id=pk)
    comments = BlogComment.objects.all()
    user = request.user

    form = CommentForm(request.POST or None)
    if form.is_valid():
        # User must login first to make a comment
        if user.is_authenticated:
            comment = form.cleaned_data.get("comment")
            BlogComment.objects.create(blog=blog, user=user, comment=comment)
            return redirect("blog:detail", pk)
        else:
            return redirect("account:login")
    context = {'blog': blog, 'comments': comments, 'form': form}
    return render(request, "blog/blog_detail.html", context)
