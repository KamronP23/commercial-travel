from django.db import models


class FrequentTravelGroup(models.Model):
    group_name = models.CharField(max_length=50)

    def __str__(self):
        return self.group_name


class Client(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50)
    dob = models.DateField()
    email = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=5)
    state = models.CharField(max_length=50)
    home_phone = models.CharField(max_length=12)
    cell_phone = models.CharField(max_length=12)

    frequent_travel_group = models.ForeignKey(
        FrequentTravelGroup,
        related_name="frequent_travel_group",
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )


class Flight(models.Model):
    flight_details = models.CharField(max_length=50)
    airline = models.CharField(max_length=50)
    departure_city = models.CharField(max_length=50)
    departure_airport = models.CharField(max_length=10)
    arrival_city = models.CharField(max_length=50)
    arrival_airport = models.CharField(max_length=10)
    layover = models.CharField(max_length=50, blank=True, null=True)
    departure_time = models.DateTimeField(auto_now_add=False)
    arrival_time = models.DateTimeField(auto_now_add=False)
    flight_number_of_travelers = models.SmallIntegerField()
    flight_total_cost = models.SmallIntegerField()

    def __str__(self):
        return self.flight_details


class Hotel(models.Model):
    hotel_details = models.CharField(max_length=50)
    hotel_name = models.CharField(max_length=50)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    hotel_city = models.CharField(max_length=50)
    hotel_country = models.CharField(max_length=50)
    hotel_number_of_guests = models.SmallIntegerField()
    hotel_total_cost = models.SmallIntegerField()

    def __str__(self):
        return self.hotel_details


class Cruise(models.Model):
    cruise_details = models.CharField(max_length=50)
    cruise_line = models.CharField(max_length=50)
    cruise_departure_city = models.CharField(max_length=50)
    cruise_departure_date = models.DateField()
    cruise_arrival_date = models.DateField()
    cruise_number_of_passengers = models.SmallIntegerField()
    cruise_total_cost = models.SmallIntegerField()

    def __str__(self):
        return self.cruise_details


class Package(models.Model):
    trip_name = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    total_travelers = models.SmallIntegerField()
    package_total_cost = models.SmallIntegerField()

    clients = models.ManyToManyField(
        Client,
        related_name="trips",
        blank=True
        )

    groups = models.ManyToManyField(
        FrequentTravelGroup,
        related_name="trips",
        blank=True
        )
    flights = models.ManyToManyField(
        Flight,
        related_name="trips",
        blank=True
        )

    hotels = models.ManyToManyField(
        Hotel,
        related_name="trips",
        blank=True
        )

    cruises = models.ManyToManyField(
        Cruise,
        related_name="trips",
        blank=True
        )

    def __str__(self):
        return self.trip_name
