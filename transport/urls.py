from django.urls import path, re_path
from transport import views


urlpatterns = [
  path('', views.index, name='index'),
  ## access through url
  re_path(r'^arrivals/(?P<stop>.+)/$', views.ArrivalTimesOfStop.as_view()),
  re_path(r'^day-trips/(?P<day>.+)/$', views.TripsOnGivenDay.as_view()),
  ## access through the forms
  path('arrivals-form/', views.ArrivalTimesOfStop.as_view()),
  path('day-trips-form/', views.TripsOnGivenDay.as_view()),
 ]