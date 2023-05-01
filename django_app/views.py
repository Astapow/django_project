from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django_app.forms import CreateNewBlog, Register, AuthenticationForm, CreateNewComment
from django_app.models import BlogPost, Comment, Topic
from django.contrib.auth.decorators import login_required


@login_required(login_url='login/')
def blogs(request):
    topics = Topic.objects.all()
    search_text = request.GET.get('search_text')
    topic_id = request.GET.get('topic')

    if search_text:
        blog_posts = BlogPost.objects.filter(title__icontains=search_text)
    elif topic_id:
        blog_posts = BlogPost.objects.filter(topic__in=[topic_id])
    else:
        blog_posts = BlogPost.objects.all()
    return render(request, 'home_page.html', {'blog_posts': blog_posts, 'topics': topics})


def about_site(request):
    return HttpResponse("about your site")


@login_required(login_url='/login/')
def dynamic_blog(request, slug):
    post = BlogPost.objects.get(slug=slug)
    comments = Comment.objects.filter(blog_post=post)
    return render(request, 'dynamic_blog.html', {"slug": slug, 'post': post, 'comments': comments})


def add_comment(request, slug):
    if not slug:
        raise Http404('Slug parameter is missing')
    post = BlogPost.objects.get(slug=slug)
    if request.method == 'POST':
        form = CreateNewComment(request.POST)
        if form.is_valid():
            content = form.cleaned_data.get('content')
            author = request.user
            blog_post = post
            create_comment = Comment.objects.create(author=author, blog_post=blog_post, content=content)
            return render(request, 'create_comment_was_valid.html',
                          {'create_comment': create_comment, 'form': form, 'post': post})
    else:
        form = CreateNewComment()
    return render(request, 'create_comment.html', {'form': form, 'post': post})


@login_required(login_url='/login/')
def create_new_post(request):
    if request.method == 'POST':

        form = CreateNewBlog(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            author = request.user
            new_post = BlogPost.objects.create(author=author, title=title, content=content)
            for topic in form.cleaned_data.get('topic'):
                new_post.topic.add(topic)
            return redirect('home')

    else:
        form = CreateNewBlog()

    return render(request, 'create_new_blog.html', {'form': form})


def update_post(request, slug):
    return HttpResponse(f"{slug} update post")


def delete_post(request, slug):
    return HttpResponse(f"{slug} delete post")


def users_personal_page(request, username):
    return HttpResponse(f"user's personal page {username}")


def change_password(request):
    return HttpResponse("change_password")


def user_registration(request):
    if request.method == 'POST':
        register = Register(request.POST)
        if register.is_valid():
            create_new_user = register.save(commit=False)
            create_new_user.set_password(register.cleaned_data.get('password'))
            create_new_user.save()
            return render(request, 'register_was_valid.html', {'create_new_user': create_new_user})

    else:
        register = Register()

    return render(request, 'register.html', {'register': register})


def login_user(request):
    if request.method == 'POST':
        log_in = AuthenticationForm(request.POST)
        if log_in.is_valid():
            login(request, log_in.user)
            return HttpResponseRedirect('/')

    else:
        log_in = AuthenticationForm()

    return render(request, 'login.html', {'login': log_in})


def logout_user(request):
    logout(request)
    return redirect('login')
