from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.utils.text import slugify
from django.contrib import messages
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from .models import Post, Comment, Favourite
from .forms import CommentForm, PostForm


# Create your views here.
class PostList(generic.ListView):
    """
    List all published posts
    """
    queryset = Post.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 6


class MyPosts(LoginRequiredMixin, generic.ListView):
    """
    List the post made by the present logged in user
    """
    template_name = "blog/my_posts.html"
    paginate_by = 6

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)


class Continents(generic.ListView):
    """
    List the posts from a specific continent.
    """
    template_name = "blog/continents.html"
    paginate_by = 6

    CONTINENT_SLUGS = {
        "south-central-america": 0,
        "north-america": 1,
        "europe": 2,
        "africa": 3,
        "asia": 4,
        "australia": 5,
    }

    def get_queryset(self):
        continent_slug = self.kwargs.get("continent_slug")
        continent_id = self.CONTINENT_SLUGS.get(continent_slug)
        return Post.objects.filter(continent=continent_id, status=1)


class AddPost(LoginRequiredMixin, generic.CreateView):
    """
    Add blog post
    """

    template_name = "blog/add_post.html"
    model = Post
    form_class = PostForm
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        """Checks that slug is unique or add suffix"""
        base_slug = slugify(form.instance.title)
        slug = base_slug
        counter = 1
        while Post.objects.filter(slug=slug).exists():
            slug = f"{base_slug}-{counter}"
            counter += 1
        form.instance.slug = slug
        form.instance.author = self.request.user
        response = super().form_valid(form)
        messages.success(
            self.request, "Your post has been created, awaits admin approval!"
        )
        return response


class EditPost(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    """
    View to edit a post.
    """
    template_name = "blog/edit_post.html"
    model = Post
    form_class = PostForm
    success_url = reverse_lazy("my_posts")

    def test_func(self):
        return self.request.user == self.get_object().author

    def form_valid(self, form):
        """
        Checks that slug is unique or add suffix,
        sets status to 0 (unpublished)
        """
        base_slug = slugify(form.instance.title)
        slug = base_slug
        counter = 1
        while Post.objects.filter(slug=slug).exists():
            slug = f"{base_slug}-{counter}"
            counter += 1
        form.instance.slug = slug
        form.instance.status = 0
        response = super().form_valid(form)
        messages.success(
            self.request, "Your post has been updated, awaits admin approval!"
        )
        return response


class DeletePost(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    """
    View to delete a post.
    """

    model = Post
    success_url = reverse_lazy("my_posts")

    def test_func(self):
        return self.request.user == self.get_object().author

    def form_valid(self, form):
        messages.success(self.request, "Post deleted!")
        return super().form_valid(form)


def post_detail(request, slug):
    """
    Display an individual blog post.
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()
    is_favourited = False

    if request.user.is_authenticated:
        is_favourited = Favourite.objects.filter(
            user=request.user, post=post).exists()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                "Comment submitted, awaits admin approval"
            )

    comment_form = CommentForm()

    return render(
        request,
        "blog/post_detail.html",
        {
            "post": post,
            "is_favourited": is_favourited,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )


@login_required
def comment_edit(request, slug, comment_id):
    """
    View to edit a comment.
    """
    if request.method == "POST":
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                "Comment Updated, awaits admin approval"
            )
        else:
            messages.add_message(request, messages.ERROR,
                                 "Error updating the comment!")

    return HttpResponseRedirect(reverse("post_detail", args=[slug]))


@login_required
def comment_delete(request, slug, comment_id):
    """
    View to delete a comment.
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, "Comment deleted!")
    else:
        messages.add_message(
            request,
            messages.ERROR,
            "Deletion failed, you can only delete your own comments!",
        )

    return HttpResponseRedirect(reverse("post_detail", args=[slug]))


@login_required
def toggle_favourite(request, post_id):
    """
    View to add or remove a post from favourites when on post_detail.
    """
    post = get_object_or_404(Post, id=post_id)
    favourite, created = Favourite.objects.get_or_create(
        user=request.user, post=post)
    if not created:
        favourite.delete()
    return HttpResponseRedirect(reverse("post_detail", args=[post.slug]))


@login_required
def remove_favourite(request, post_id):
    """
    View to remove post from favourites when on "Favourites".
    """
    post = get_object_or_404(Post, id=post_id)
    favourite, created = Favourite.objects.get_or_create(
        user=request.user, post=post)
    if not created:
        favourite.delete()
    return HttpResponseRedirect(reverse("my_favourites"))


@login_required
def my_favourites(request):
    """
    View to list my favourites.
    """
    favourites = Favourite.objects.filter(
        user=request.user).select_related("post")
    return render(
        request, "blog/my_favourites.html", {"favourites": favourites})
