from django.contrib import admin
from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget
from .models import Post, Comment


class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditor5Widget(
        attrs={"class": "django_ckeditor_5"},
        config_name="default"  # or your custom config name
    ))

    class Meta:
        model = Post
        fields = "__all__"


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    list_display = ('title', 'slug', 'status', 'created_on',)
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on',)
    prepopulated_fields = {'slug': ('title',)}

# Register your models here.

admin.site.register(Comment)