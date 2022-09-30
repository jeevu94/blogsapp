from django.contrib.auth import get_user_model
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from tinymce.models import HTMLField

from blogsapp.utils.helpers import random_n_token
from blogsapp.utils.managers import BaseObjectManagerQuerySet
from blogsapp.utils.models import BaseModel


class Blog(BaseModel):
    """Blogs model"""

    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, blank=True)
    description = HTMLField()
    ta_title = models.CharField(max_length=255)
    ta_description = HTMLField()

    author = models.ForeignKey(
        get_user_model(), related_name="blogs", on_delete=models.CASCADE
    )
    cover_image = models.ImageField(upload_to="blog-images/", blank=True, null=True)

    objects = BaseObjectManagerQuerySet.as_manager()

    class Meta:
        verbose_name = "blog"
        verbose_name_plural = "blogs"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title) + "-" + random_n_token()
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("blog:blog_detail_view", args=[self.slug])
