from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from hackathon.models import Hackathon


class Participant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hackathons = models.ManyToManyField(
        Hackathon, through='ParticipantHackathon')

    def __str__(self):
        return self.user.username


class ParticipantHackathon(models.Model):
    participant = models.ForeignKey(
        Participant, on_delete=models.CASCADE)
    hackathon = models.ForeignKey(Hackathon, on_delete=models.CASCADE)
    submission_file = models.FileField(
        upload_to='hackathon_submissions/file/', null=True, blank=True)
    submission_image = models.ImageField(
        upload_to='hackathon_submissions/image/', null=True, blank=True)
    submission_link = models.URLField(null=True, blank=True)

    def clean(self):
        from django.core.exceptions import ValidationError
        if self.submission_file and self.hackathon.submission_type != 'file':
            raise ValidationError(
                'Submission is only allowed for File submission type.')
        if self.submission_image and self.hackathon.submission_type != 'image':
            raise ValidationError(
                'Submission is only allowed for Image submission type.')
        if self.submission_link and self.hackathon.submission_type != 'link':
            raise ValidationError(
                'Submission is only allowed for Link submission type.')

    def __str__(self) -> str:
        return (self.participant.__str__() + '@' + self.hackathon.__str__())

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('participant:submission', args=[str(self.id)])
