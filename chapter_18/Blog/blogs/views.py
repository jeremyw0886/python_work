from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog, Post
from .forms import BlogForm, PostForm


def index(request):
    """Home page that shows all posts and blogs."""
    posts = Post.objects.all().order_by("-created_at")
    blogs = Blog.objects.all().order_by("title")
    context = {
        "posts": posts,
        "blogs": blogs,  # Use "blogs" as the key, not "blogs:"
    }
    # Pass the entire context dictionary to the template
    return render(request, "blogs/index.html", context)


def new_blog(request):
    """Page for creating a new blog."""
    if request.method != "POST":
        form = BlogForm()
    else:
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("blogs:index")
    return render(request, "blogs/new_blog.html", {"form": form})


def new_post(request, blog_id):
    """Page for creating a new post for a specific blog."""
    blog = get_object_or_404(Blog, id=blog_id)
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


def edit_post(request, post_id):
    """Page for editing an existing post."""
    post = get_object_or_404(Post, id=post_id)
    if request.method != "POST":
        form = PostForm(instance=post)
    else:
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("blogs:index")
    context = {"form": form, "post": post}
    return render(request, "blogs/edit_post.html", context)
