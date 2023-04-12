from django.http import HttpResponse


def blogs(request):
    return HttpResponse("it`s blogs")


def about_site(request):
    return HttpResponse("about your site")


def dynamic_blog(request, slug):
    return HttpResponse(f"show one dynamic blogs {slug}")


def add_comment(request, slug):
    return HttpResponse(f"{slug} add new comment")


def create_new_post(request):
    return HttpResponse("create new post")


def update_post(request, slug):
    return HttpResponse(f"{slug} update post")


def delete_post(request, slug):
    return HttpResponse(f"{slug} delate post")


def users_personal_page(request, username):
    return HttpResponse(f"user's personal page {username}")


def change_password(request):
    return HttpResponse("change_password")


def user_registration(request):
    return HttpResponse("User registration")


def login(request):
    return HttpResponse("login")


def logout(request):
    return HttpResponse("logout")
