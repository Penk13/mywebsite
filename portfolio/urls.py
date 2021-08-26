from django.urls import path

from .views import (
    portfolio,
    # read_blog,
)


app_name = 'portfolio'
urlpatterns = [
    path('', portfolio, name='homepage'),
    # path('blog/<int:pk>/', read_blog, name='blog'),
]
