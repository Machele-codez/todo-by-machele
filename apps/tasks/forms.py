from .models import Task
from django import forms
from django.http import request
import datetime, pytz

class TaskForm(forms.ModelForm):
    due_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    due_time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))

    class Meta:
        model = Task
        fields = ('text', 'priority')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].widget.attrs['placeholder'] = 'Add Task Here'

    def clean(self):
        due_date = self.cleaned_data['due_date']
        due_time = self.cleaned_data['due_time']
        due_datetime = datetime.datetime(year=due_date.year, month=due_date.month, day=due_date.day) + datetime.timedelta(hours=due_time.hour, minutes=due_time.minute) #? add both date and time
        due_datetime = due_datetime.replace(tzinfo=datetime.timezone.utc)
        #? if due datetime is before current date then raise an error
        if due_datetime < datetime.datetime.today().replace(tzinfo=datetime.timezone.utc):
            raise forms.ValidationError(
            'due date and time cannot occur before current date',
            'backdating'
        )