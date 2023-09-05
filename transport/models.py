# This is an auto-generated Django model module.
# It has been modified to allow innerjoins between the tables, according to the GTFS filesystem relations: https://developers.google.com/transit/gtfs/reference
from django.db import models


class Agency(models.Model):
    agency_id = models.CharField(max_length=100, primary_key=True)
    agency_name = models.CharField(max_length=100)
    agency_url = models.CharField(max_length=100)
    agency_timezone = models.CharField(max_length=100)
    agency_lang = models.CharField(max_length=100)
    agency_phone = models.CharField(max_length=100)

    def __str__(self):
        return self.agency_id

    class Meta:
        managed = False
        db_table = 'agency'


class Calendar(models.Model):
    service_id = models.CharField(max_length=100, primary_key=True)
    monday = models.CharField(max_length=100)
    tuesday = models.CharField(max_length=100)
    wednesday = models.CharField(max_length=100)
    thursday = models.CharField(max_length=100)
    friday = models.CharField(max_length=100)
    saturday = models.CharField(max_length=100)
    sunday = models.CharField(max_length=100)
    start_date = models.CharField(max_length=100)
    end_date = models.CharField(max_length=100)

    def __str__(self):
        return self.service_id

    class Meta:
        managed = False
        db_table = 'calendar'


class CalendarDates(models.Model):
    service_id = models.TextField(blank=True, null=True)
    date = models.TextField(blank=True, null=True)
    exception_type = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.date

    class Meta:
        managed = False
        db_table = 'calendar_dates'


class FeedInfo(models.Model):
    feed_publisher_name = models.TextField(blank=True, null=True)
    feed_publisher_url = models.TextField(blank=True, null=True)
    feed_lang = models.TextField(blank=True, null=True)
    feed_version = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.feed_publisher_name

    class Meta:
        managed = False
        db_table = 'feed_info'


class Notes(models.Model):
    note_id = models.TextField(blank=True, null=True)
    note_text = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.note_id

    class Meta:
        managed = False
        db_table = 'notes'


class Routes(models.Model):
    route_id = models.CharField(max_length=200, primary_key=True)
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE)
    route_short_name = models.CharField(max_length=100)
    route_long_name = models.CharField(max_length=100)
    route_desc = models.CharField(max_length=100)
    route_type = models.CharField(max_length=100)
    route_color = models.CharField(max_length=100)
    route_text_color = models.CharField(max_length=100)

    def __str__(self):
        return self.route_id

    class Meta:
        managed = False
        db_table = 'routes'


class Shapes(models.Model):
    shape_id = models.CharField(max_length=200, primary_key=True)
    shape_pt_lat = models.CharField(max_length=100)
    shape_pt_lon = models.CharField(max_length=100)
    shape_pt_sequence = models.CharField(max_length=100)
    shape_dist_traveled = models.CharField(max_length=100)

    def __str__(self):
        return self.shape_id

    class Meta:
        managed = False
        db_table = 'shapes'


class Stops(models.Model):
    stop_id = models.CharField(max_length=100, primary_key=True)
    stop_code = models.CharField(max_length=100)
    stop_name = models.CharField(max_length=100)
    stop_lat = models.CharField(max_length=100)
    stop_lon = models.CharField(max_length=100)
    location_type = models.CharField(max_length=100)
    parent_station = models.CharField(max_length=100)
    wheelchair_boarding = models.CharField(max_length=100)
    platform_code = models.CharField(max_length=100)
    stop_timezone = models.CharField(max_length=100)

    def __str__(self):
        return self.stop_id

    class Meta:
        managed = False
        db_table = 'stops'


class Trips(models.Model):
    route = models.ForeignKey(Routes, on_delete=models.CASCADE)
    service = models.ForeignKey(Calendar, on_delete=models.CASCADE)
    trip_id = models.CharField(max_length=200, primary_key=True)
    trip_headsign = models.CharField(max_length=100)
    trip_short_name = models.CharField(max_length=100)
    direction_id = models.CharField(max_length=100)
    block_id = models.CharField(max_length=100)
    shape_id = models.CharField(max_length=100)
    wheelchair_accessible = models.CharField(max_length=100)
    bikes_allowed = models.CharField(max_length=100)
    trip_note = models.CharField(max_length=100)
    route_direction = models.CharField(max_length=200)

    def __str__(self):
        return self.route_id

    class Meta:
        managed = False
        db_table = 'trips'

class StopTimes(models.Model):
    trip = models.ForeignKey(Trips, on_delete=models.CASCADE)
    arrival_time = models.CharField(max_length=100)
    departure_time = models.CharField(max_length=100)
    stop = models.ForeignKey(Stops, on_delete=models.CASCADE)
    stop_sequence = models.CharField(max_length=100)
    stop_headsign = models.CharField(max_length=100)
    pickup_type = models.CharField(max_length=100)
    drop_off_type = models.CharField(max_length=100)
    timepoint = models.CharField(max_length=100)
    stop_note = models.CharField(max_length=100)
    shape_dist_traveled = models.CharField(max_length=100)

    def __str__(self):
        return self.trip_id

    class Meta:
        managed = False
        db_table = 'stop_times'

