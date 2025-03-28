from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Blog, Post
from .forms import BlogForm, PostForm

def index(request):
    """Home page that shows all posts and blogs."""
    posts = Post.objects.all().order_by("-created_at")
    blogs = Blog.objects.all().order_by("title")
    context = {
        "posts": posts,
        "blogs": blogs,
    }
    return render(request, "blogs/index.html", context)

@login_required
def new_blog(request):
    """Page for creating a new blog. Only logged-in users can create a blog,
    and the new blog is automatically connected to the current user."""
    if request.method != "POST":
        form = BlogForm()
    else:
        form = BlogForm(request.POST)
        if form.is_valid():
            new_blog = form.save(commit=False)
            new_blog.owner = request.user  # Connect the blog to the current user
            new_blog.save()
            return redirect("blogs:index")
    return render(request, "blogs/new_blog.html", {"form": form})

@login_required
def new_post(request, blog_id):
    """Page for creating a new post for a specific blog.Only logged-in users 
    can add posts, and they can only add posts to their own blogs."""
    blog = get_object_or_404(Blog, id=blog_id)
    if blog.owner != request.user:
        raise Http404("You cannot add a post to a blog you do not own.")
    if request.method != "POST":
        form = PostForm()
    else:
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.blog = blog
            new_post.save()
            return redirect("blogs:index")
    context = {"form": form, "blog": blog}
    return render(request, "blogs/new_post.html", context)

@login_required
def edit_post(request, post_id):
    """Page for editing an existing post.
    Only the owner of the blog to which the post belongs may edit it."""
    post = get_object_or_404(Post, id=post_id)
    if post.blog.owner != request.user:
        raise Http404("You cannot edit a post you do not own.")
    if request.method != "POST":
        form = PostForm(instance=post)
    else:
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("blogs:index")
    context = {"form": form, "post": post}
    return render(request, "blogs/edit_post.html", context)