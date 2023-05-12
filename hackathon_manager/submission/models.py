from datetime import datetime
from django.db import models
from django.urls import reverse
from hackathon.models import Participant, Hackathon
from django.core.exceptions import ValidationError


class Submission(models.Model):
    participant = models.ForeignKey(
        Participant, on_delete=models.CASCADE)
    hackathon = models.ForeignKey(Hackathon, on_delete=models.CASCADE)
    submission_file = models.FileField(
        upload_to='hackathon_submissions/file/', null=True, blank=True)
    submission_image = models.ImageField(
        upload_to='hackathon_submissions/image/', null=True, blank=True)
    submission_link = models.URLField(null=True, blank=True)

    def __str__(self) -> str:
        return (self.participant.__str__() + '@' + self.hackathon.__str__())

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('submission:list', args=[str(self.id)])
