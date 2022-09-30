from django.urls import path

from blogsapp.users.views import (
    user_detail_view,
    user_logout_view,
    user_redirect_view,
    user_update_view,
)

app_name = "users"
urlpatterns = [
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("<str:username>/", view=user_detail_view, name="detail"),
    path("logout/", view=user_logout_view, name="logout"),
]
