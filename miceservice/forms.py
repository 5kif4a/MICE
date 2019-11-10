from django.forms import ModelForm
from miceservice.models import *


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = 'Name of event'
        self.fields['date'].label = 'Date of the event'
        self.fields['place'].label = 'Location'
