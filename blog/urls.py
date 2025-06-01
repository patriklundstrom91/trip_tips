from django.urls import path
from . import views


urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path("add_post", views.AddPost.as_view(), name="add_post"),
    path("my_posts", views.MyPosts.as_view(), name="my_posts"),
    path("continents/<slug:continent_slug>/", views.Continents.as_view(), name="continents"),
    path("delete/<slug:pk>/", views.DeletePost.as_view(), name="delete_post"),
    path("edit/<slug:pk>/", views.EditPost.as_view(), name="edit_post"),
    path("favourite/<int:post_id>/toggle", views.toggle_favourite, name="toggle_favourite"),
    path("favourite/<int:post_id>/remove", views.remove_favourite, name="remove_favourite"),
    path("my_favourites/", views.my_favourites, name="my_favourites"),
    path(
        "<slug:slug>/edit_comment/<int:comment_id>",
        views.comment_edit,
        name="comment_edit",
    ),
    path(
        "<slug:slug>/delete_comment/<int:comment_id>",
        views.comment_delete,
        name="comment_delete",
    ),
    path("<slug:slug>/", views.post_detail, name="post_detail"),
]
