from django.contrib import admin
from friendly_agent.models import (
    Client,
    FrequentTravelGroup,
    Package, Flight,
    Hotel,
    Cruise
    )


@admin.register(FrequentTravelGroup)
class FrequentTravelGroupAdmin(admin.ModelAdmin):
    list_display = (
        "group_name",
    )


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "middle_name",
        "last_name",
        "dob",
        "email",
        "street",
        "city",
        "zipcode",
        "state",
        "home_phone",
        "cell_phone",
        "frequent_travel_group"
    )


@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    list_display = (
        "flight_details",
        "airline",
        "departure_city",
        "departure_airport",
        "arrival_city",
        "arrival_airport",
        "layover",
        "departure_time",
        "arrival_time",
        "flight_number_of_travelers",
        "flight_total_cost"
    )


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = (
        "hotel_details",
        "hotel_name",
        "check_in_date",
        "check_out_date",
        "hotel_city",
        "hotel_country",
        "hotel_number_of_guests",
        "hotel_total_cost"
        )


@admin.register(Cruise)
class CruiseAdmin(admin.ModelAdmin):
    list_display = (
        "cruise_details",
        "cruise_line",
        "cruise_departure_city",
        "cruise_departure_date",
        "cruise_arrival_date",
        "cruise_number_of_passengers",
        "cruise_total_cost"
        )

@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = (
        "trip_name",
        "start_date",
        "end_date",
        "total_travelers",
        "package_total_cost"
    )
