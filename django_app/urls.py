from django.urls import path, include

urlpatterns = [
    path('api/', include('django_app.api.urls')),
]