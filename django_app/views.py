from django.http import HttpResponse
from django.shortcuts import render


def blogs(request):
    return render(request, 'home_page.html')


def about_site(request):
    return HttpResponse("about your site")


def dynamic_blog(request, slug):
    return render(request, 'dynamic_blog.html', {"slug": slug})


def add_comment(request, slug):
    return HttpResponse(f"{slug} add new comment")


def create_new_post(request):
    return render(request, 'create_new_blog.html')


def update_post(request, slug):
    return HttpResponse(f"{slug} update post")


def delete_post(request, slug):
    return HttpResponse(f"{slug} delete post")


def users_personal_page(request, username):
    return HttpResponse(f"user's personal page {username}")


def change_password(request):
    return HttpResponse("change_password")


def user_registration(request):
    return render(request, 'register.html')


def login(request):
    return render(request, 'login.html')


def logout(request):
    return HttpResponse("logout")
