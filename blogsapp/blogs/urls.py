from django.urls import path

from blogsapp.blogs.views import (
    BlogsView,
    CreateBlogView,
    DetailBlogView,
    UpdateBlogView,
)

app_name = "blog"

urlpatterns = [
    path(
        "",
        BlogsView.as_view(),
        name="homepage_view",
    ),
    path("blogs/new", CreateBlogView.as_view(), name="create_blog_view"),
    path("blogs/update/<str:slug>", UpdateBlogView.as_view(), name="update_blog_view"),
    path("blogs/<str:slug>", DetailBlogView.as_view(), name="blog_detail_view"),
]
