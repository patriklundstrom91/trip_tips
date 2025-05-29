from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget
from .models import Comment, Post


class PostForm(forms.ModelForm):
    """
    Form to add a post
    """

    class Meta:
        model = Post
        fields = [
            "title",
            "featured_image",
            "content",
            "excerpt",
            "continent",
        ]

        labels = {
            "title": "Post title",
            "featured_image": "Post main image",
            "excerpt": "Post intro text/ Summary",
        }


class CommentForm(forms.ModelForm):
    """
    Form to add a comment
    """

    class Meta:
        model = Comment
        fields = ("body",)
        labels = {
            "body": "Comment",
        }
