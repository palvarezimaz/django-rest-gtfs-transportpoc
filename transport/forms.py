from django import forms
from .models import StopTimes, Stops


class ArrivalTimesForm(forms.Form):
    station_names = Stops.objects.filter(
        stop_id__in=StopTimes.objects.all().values_list(
        'stop_id', flat=True).distinct()).values_list('stop_name', flat=True).order_by('stop_name')
    station = forms.ModelChoiceField(queryset=station_names)


class AllTripsForm(forms.Form):
    CHOICES = [('---------', '---------'),('monday', 'Monday'), ('tuesday', 'Tuesday'), ('wednesday', 'Wednesday'),
               ('thursday', 'Thursday'), ('friday', 'Friday'), ('saturday', 'Saturday'), ('sunday', 'Sunday')]
    days = forms.ChoiceField(choices=CHOICES)