from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import ValidationError
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Submission
from .forms import SubmissionCreateForm, SubmissionUpdateForm
from hackathon.models import Participant, Hackathon


class UserSubmissionListView(LoginRequiredMixin, ListView):
    model = Submission
    template_name = 'submission/user_submission_list.html'
    context_object_name = 'submissions'

    def get_queryset(self):
        user = Participant.objects.filter(user=self.request.user)[0]
        queryset = Submission.objects.filter(participant=user)
        return queryset


class SubmissionCreateView(LoginRequiredMixin, CreateView):
    model = Submission
    form_class = SubmissionCreateForm
    template_name = 'submission/submission_create.html'
    success_url = reverse_lazy('submission:list')

    def form_valid(self, form):
        form.instance.participant = Participant.objects.filter(
            user=self.request.user,
            hackathon__slug=self.kwargs.get("hackathon_slug")
        ).get()
        form.instance.hackathon = get_object_or_404(
            Hackathon, slug=self.kwargs.get("hackathon_slug"))
        start_date = form.instance.hackathon.start_datetime.strftime(
            '%d/%m/%Y %H:%M')
        start = datetime.strptime(
            start_date, '%d/%m/%Y %H:%M')
        if datetime.now() < start:
            raise ValidationError(
                'Submission is only allowed once the Hackathon starts.')
        end_date = form.instance.hackathon.end_datetime.strftime(
            '%d/%m/%Y %H:%M')
        end = datetime.strptime(
            end_date, '%d/%m/%Y %H:%M')
        if datetime.now() > end:
            raise ValidationError(
                'Submission is not allowed once the Hackathon ends.')
        if form.instance.submission_file and form.instance.hackathon.submission_type != 'file':
            raise ValidationError(
                'Submission is only allowed for File submission type.')
        if form.instance.submission_image and form.instance.hackathon.submission_type != 'image':
            raise ValidationError(
                'Submission is only allowed for Image submission type.')
        if form.instance.submission_link and form.instance.hackathon.submission_type != 'link':
            raise ValidationError(
                'Submission is only allowed for Link submission type.')
        return super().form_valid(form)


class SubmissionUpdateView(LoginRequiredMixin, UpdateView):
    model = Submission
    form_class = SubmissionUpdateForm
    template_name = 'submission/submission_update.html'
    success_url = reverse_lazy('submission:list')

    def form_valid(self, form):
        start_date = form.instance.hackathon.start_datetime.strftime(
            '%d/%m/%Y %H:%M')
        start = datetime.strptime(
            start_date, '%d/%m/%Y %H:%M')
        if datetime.now() < start:
            raise ValidationError(
                'Submission is only allowed once the Hackathon starts.')
        end_date = form.instance.hackathon.end_datetime.strftime(
            '%d/%m/%Y %H:%M')
        end = datetime.strptime(
            end_date, '%d/%m/%Y %H:%M')
        if datetime.now() > end:
            raise ValidationError(
                'Submission is not allowed once the Hackathon ends.')
        if form.instance.submission_file and form.instance.hackathon.submission_type != 'file':
            raise ValidationError(
                'Submission is only allowed for File submission type.')
        if form.instance.submission_image and form.instance.hackathon.submission_type != 'image':
            raise ValidationError(
                'Submission is only allowed for Image submission type.')
        if form.instance.submission_link and form.instance.hackathon.submission_type != 'link':
            raise ValidationError(
                'Submission is only allowed for Link submission type.')
        return super().form_valid(form)


class SubmissionDetailView(LoginRequiredMixin, DetailView):
    model = Submission
    template_name = 'submission/submission_detail.html'


class SubmissionDeleteView(LoginRequiredMixin, DeleteView):
    model = Submission
    template_name = 'submission/submission_confirm_delete.html'
    success_url = reverse_lazy('submission:list')
