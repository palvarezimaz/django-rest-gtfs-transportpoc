from django.test import TestCase
from django.urls import include, path, reverse
from rest_framework.test import APITestCase, URLPatternsTestCase


##All test-units fail as Django fails to build up the test database

class ServerRunningTest(TestCase):
  def test_test(self):
    """test framework works"""
    tx = 'test framework'
    self.assertEqual('test framework', tx)



#   def test_api_returns_ok_response(self):
#     """Server returns 200 when accessed"""
#     url = 'http://localhost:8000/'
#     response = self.client.get(url)
#     self.assertEqual(response.status_code, 200)


# ### Tests fail on building the Test-Database..##???
# class ApiResponsesTest(TestCase):

#   def test_trips_on_a_monday_return_ok_response(self):
#     """Api returns 200 ok when queried about trips on a tuesday
#     """
#     url = 'http://localhost:8000/day-trips/tuesday'
#     response = self.client.get(url)
#     self.assertEqual(response.status_code, 200)

#   def test_arrival_times_on_station(self):
#     """Api returns 200 ok when queried about arrival times on a station"""
#     url = 'http://localhost:8000/arrivals/2155269'
#     response = self.client.get(url)
#     self.assertEqual(response.status_code, 200)


# class TripsTests(APITestCase, URLPatternsTestCase):
#   urlpatterns = [
#     path('', include('transport.urls'))
#   ]

#   def test_get_response(self):
#     """Ensure server responds"""
#     url = 'http://localhost:8000/arrivals/2155269'
#     response = self.client.get(url, format='json')
#     self.assertEqual(response.status_code, 200)