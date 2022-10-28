
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),                 # Starting page. Welcome text and posts list.
    path("posts"),          # List with all posts.
    path("posts/<slug>")    # /posts/post-name Shows full blog post.
]
