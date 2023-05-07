from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DetailView, DeleteView, RedirectView
from .models import Hackathon, Participant
from .forms import HackathonCreateForm, HackathonUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

# Hackathon Views


class HackathonCreateView(LoginRequiredMixin, CreateView):
    model = Hackathon
    form_class = HackathonCreateForm
    template_name = 'hackathon/hackathon_form.html'
    success_url = reverse_lazy('hackathon:list')


class HackathonModifyView(LoginRequiredMixin, UpdateView):
    model = Hackathon
    form_class = HackathonUpdateForm
    template_name = 'hackathon/hackathon_form.html'
    success_url = reverse_lazy('hackathon:list')


class HackathonListView(ListView):
    model = Hackathon
    template_name = 'hackathon/hackathon_list.html'
    context_object_name = 'hackathons'


class HackathonDetailView(DetailView):
    model = Hackathon
    template_name = 'hackathon/hackathon_detail.html'
    context_object_name = 'hackathon'


class HackathonDeleteView(LoginRequiredMixin, DeleteView):
    model = Hackathon
    success_url = reverse_lazy('hackathon:list')

# Participant Views


class Register(LoginRequiredMixin, RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse("hackathon:detail", kwargs={"slug": self.kwargs.get("slug")})

    def get(self, request, *args, **kwargs):
        hackathon = get_object_or_404(Hackathon, slug=self.kwargs.get("slug"))

        try:
            Participant.objects.create(
                user=self.request.user, hackathon=hackathon)

        except IntegrityError:
            messages.warning(
                self.request, f"Already registered for {hackathon.title}")

        else:
            messages.success(
                self.request, f"You are now registered for {hackathon.title} hackathon.")

        return super().get(request, *args, **kwargs)


class Unregister(LoginRequiredMixin, RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse("hackathon:list", kwargs={"slug": self.kwargs.get("slug")})

    def get(self, request, *args, **kwargs):
        try:
            participants = Participant.objects.filter(
                user=self.request.user,
                hackathon__slug=self.kwargs.get("slug")
            ).get()

        except Participant.DoesNotExist:
            messages.warning(
                self.request, "You can't Unregister as you not registered.")

        else:
            participants.delete()
            messages.success(
                self.request, "You have successfully Unregistered.")
        return super().get(request, *args, **kwargs)
