# Generated by Django 4.2.20 on 2025-06-01 13:04

import blog.models
import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0008_alter_post_featured_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="featured_image",
            field=cloudinary.models.CloudinaryField(
                default="placeholder",
                max_length=255,
                validators=[blog.models.image_extension_validator],
                verbose_name="image",
            ),
        ),
    ]
