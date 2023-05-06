from django.utils import timezone
from django.forms import ValidationError, ModelForm, DateTimeField
from .models import Hackathon


class HackathonForm(ModelForm):
    start_datetime = DateTimeField(input_formats=['%d/%m/%Y %H:%M'])
    end_datetime = DateTimeField(input_formats=['%d/%m/%Y %H:%M'])

    class Meta:
        model = Hackathon
        fields = ('title', 'description', 'background_image', 'hackathon_image',
                  'submission_type', 'start_datetime', 'end_datetime', 'reward_prize')

    def clean_start_datetime(self):
        start_datetime = self.cleaned_data['start_datetime']
        if start_datetime < timezone.now():
            raise ValidationError(
                "The start date and time cannot be in the past.")
        return start_datetime

    def clean_end_datetime(self):
        end_datetime = self.cleaned_data['end_datetime']
        start_datetime = self.cleaned_data.get('start_datetime')
        if start_datetime and end_datetime <= start_datetime:
            raise ValidationError(
                "The end date and time must be after the start date and time.")
        return end_datetime

    def clean_reward_prize(self):
        reward_prize = self.cleaned_data['reward_prize']
        if reward_prize <= 0:
            raise ValidationError("The reward prize must be a positive value.")
        return reward_prize
