from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DetailView
from .models import Hackathon
from .forms import HackathonCreateForm, HackathonUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin


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
