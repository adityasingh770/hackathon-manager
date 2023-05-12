from datetime import datetime
from django import forms
from django.shortcuts import get_object_or_404
from .models import Submission
from hackathon.models import Hackathon


class SubmissionCreateForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ['submission_file', 'submission_image', 'submission_link']


class SubmissionUpdateForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ['submission_file', 'submission_image', 'submission_link']
