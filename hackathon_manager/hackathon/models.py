from django.db import models
from django.urls import reverse
# from markdown import markdown
from django.utils.text import slugify


class Hackathon(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(allow_unicode=True)
    description = models.TextField()
    # description_html = models.TextField(editable=False, default='', blank=True)
    background_image = models.ImageField(
        upload_to=f'uploads/background_image/')
    hackathon_image = models.ImageField(
        upload_to=f'uploads/hackathon_image/')
    SUBMISSION_CHOICES = [
        ('image', 'Image'),
        ('file', 'File'),
        ('link', 'Link'),
    ]
    submission_type = models.CharField(
        max_length=5, choices=SUBMISSION_CHOICES)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    reward_prize = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        # self.description_html = markdown(self.description)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("hackathon:single", kwargs={"slug": self.slug})

    class Meta:
        ordering = ["start_datetime"]
