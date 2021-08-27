from django.urls import path

from .views import (
    blog_detail,
    blog_list,
    give_like,
)


app_name = 'blog'
urlpatterns = [
    path('', blog_list, name='list'),
    path('<int:pk>/', blog_detail, name='detail'),
    path('<int:pk>/give-like/', give_like, name='like'),
]
