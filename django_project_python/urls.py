"""
URL configuration for django_project_python project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django_app.views import blogs, about_site, dynamic_blog, add_comment, create_new_post, update_post, delete_post, \
    users_personal_page, user_registration, change_password, login, logout

urlpatterns = [
    path('blogs/', blogs, name='home'),  # Домашняя страница, потенциально, однажды там будут блоги :)
    path('about/', about_site),  # Потенциально тут будет страница с описанием нашего блога.
    path('', blogs, name='home'),  # должен отрабатывать тот же обработчик, что и для /blogs/
    path('<slug:slug>', dynamic_blog, name='dynamic_blog'),
    # Потенциальная страница для просмотра одного блога. Динамический контент, который потенциально будет ходить в базу данных

    path('<slug:slug>/comment/', add_comment),  # Урл для добавления коментария к посту.
    path('create/', create_new_post, name='create_post'),  # Создание нового поста
    path('<slug:slug>/update/', update_post),  # Обновление существующего поста
    path('<slug:slug>/delete/', delete_post),  # Удаление поста
    path('profile/<str:username>/', users_personal_page),  # Личная страница пользователя
    path('change_password/', change_password),  # Страничка для смены пароля
    path('register/', user_registration, name='register'),  # Регистрация пользователя
    path('login/', login, name='login'),  # Логин
    path('logout/', logout),  # Логаут

]

