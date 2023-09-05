import logging

from rest_framework import generics
from django.shortcuts import render

from .models import Stops, Calendar, Trips, StopTimes
from .serializers import StopsSerializer, TripsSerializer, ArrivalTimesSerializer
from . import forms

logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'console': {
            'format': '%(name)-12s %(levelname)-8s %(message)s'
        },
        'file': {
            'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'console'
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'formatter': 'file',
            'filename': 'transport/tmp/debug.log'
        }
    },
    'loggers': {
        '': {
            'level': 'DEBUG',
            'handlers': ['console', 'file'],
        },
        'django.request': {
            'level': 'DEBUG',
            'handlers': ['console', 'file'],
            'propagate': False,
        }
    }
})
logger = logging.getLogger(__name__)


def index(request):
  station_names_list = Stops.objects.filter(
        stop_id__in=StopTimes.objects.all().values_list(
        'stop_id', flat=True).distinct()).values_list('stop_name', 'stop_id').order_by('stop_id')

  station_names_dict = dict(station_names_list)
  return render(request, 'transport/index.html', {'arrival_form': forms.ArrivalTimesForm, 'alltrips_form': forms.AllTripsForm, 'station_names_dict': station_names_dict})


class ArrivalTimesOfStop(generics.ListAPIView):
  """
  This view displays the arrival times of trains for a given stop -all of them-, by station_id through the api of by station name through the form.
  """
  serializer_class = ArrivalTimesSerializer

  def get_queryset(self, *args, **kwargs):
    if self.request.query_params.get('station'):
      stop_name = self.request.query_params.get('station')
      queryset = StopTimes.objects.filter(stop_id=(Stops.objects.filter(stop_name=stop_name).values('stop_id'))[0]['stop_id'])
      log = [stop_name, 'through the form']

    elif self.kwargs['stop']:
      stop = self.kwargs['stop']
      queryset = StopTimes.objects.filter(stop_id=f'{stop}')
      log = [stop, 'through the url path']

    logger.info(f"All arrival times of stop: '{log[0]}' requested {log[1]}.")
    return queryset

class TripsOnGivenDay(generics.ListAPIView):
  """
  This ApiView provides a list of trips (service id, trip id and route direction) that run on a given day. It serves both the api and the form requests.
  """
  serializer_class = TripsSerializer

  def get_queryset(self, *args, **kwargs):

    if self.request.query_params.get('days'):
      day = self.request.query_params.get('days')
      log = 'through the form'
    elif self.kwargs['day']:
      day = self.kwargs['day']
      log = 'through the url path'

    queryset = Trips.objects.filter(service_id__in=Calendar.objects.filter(**{f"{day}":'1'})).values('service', 'trip_id', 'route_direction')
    logger.info(f'All trips on {day} requested {log}.')
    return queryset