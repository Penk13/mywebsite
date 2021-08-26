from django.urls import path

from .views import (
    blog_detail,
)


app_name = 'blog'
urlpatterns = [
    path('<int:pk>/', blog_detail, name='detail'),
]
