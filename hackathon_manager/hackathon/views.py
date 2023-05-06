from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import Hackathon
from .forms import HackathonForm
from django.contrib.auth.mixins import LoginRequiredMixin


class HackathonCreateView(LoginRequiredMixin, CreateView):
    model = Hackathon
    form_class = HackathonForm
    template_name = 'hackathon/hackathon_form.html'
    success_url = reverse_lazy('hackathon_list')
