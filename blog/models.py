from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from cloudinary.models import CloudinaryField
from django_ckeditor_5.fields import CKEditor5Field


STATUS = ((0, "Draft"), (1, "Published"))
CONTINENT = (
    (0, "South/Central America"),
    (1, "North America"),
    (2, "Europe"),
    (3, "Africa"),
    (4, "Asia"),
    (5, "Australia"),
)
# Create your models here.


def image_extension_validator(value):
    """
    Only validate if value is an uploaded file 
    to avoid error if no new file uploaded.
    """
    if hasattr(value, 'name'):
        validator = FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'gif'])
        validator(value)


class Post(models.Model):
    """
    Store a single blog post entry related to a User
    """

    title = models.CharField("Title", max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    featured_image = CloudinaryField("image", validators=[image_extension_validator], default="placeholder")
    content = CKEditor5Field("Post content", config_name="extends")
    excerpt = models.TextField(blank=True)
    continent = models.IntegerField(choices=CONTINENT, default=2)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} | written by {self.author}"


class Comment(models.Model):
    """
    Stores a single comment related to a User and Post
    """

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.author}"


class Favourite(models.Model):
    """
    Stores a single favourite post related to a User and Post
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="favourites")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="favourited_by")

    class Meta:
        unique_together = ("user", "post")

    def __str__(self):
        return f"{self.user} favourited {self.post}"
    