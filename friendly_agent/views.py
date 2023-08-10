from .models import (
    Client,
    FrequentTravelGroup,
    Flight,
    Hotel,
    Cruise,
    Package
    )
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import json
from .utils import ModelEncoder


class FrequentTravelGroupEncoder(ModelEncoder):
    model = FrequentTravelGroup
    properties = ["group_name", "id"]

    def get_extra_data(self, o):
        extra_data = {}

        # Clients
        clients = Client.objects.filter(frequent_travel_group=o)
        clients_data = [{
            "id": client.id,
            "first_name": client.first_name,
            "last_name": client.last_name,
            # Other relevant attributes
        } for client in clients]
        extra_data["clients"] = clients_data

        # Packages
        packages = Package.objects.filter(groups=o)
        packages_data = [{
            "id": package.id,
            "trip_name": package.trip_name,
        } for package in packages]
        extra_data["packages"] = packages_data

        return extra_data


class ClientListEncoder(ModelEncoder):
    model = Client
    properties = [
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
        "frequent_travel_group",
        "id",
    ]
    encoders = {
        "frequent_travel_group": FrequentTravelGroupEncoder(),
    }


class FlightListEncoder(ModelEncoder):
    model = Flight
    properties = [
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
        "flight_total_cost",
        "id"
    ]


class HotelListEncoder(ModelEncoder):
    model = Hotel
    properties = [
        "hotel_details",
        "hotel_name",
        "check_in_date",
        "check_out_date",
        "hotel_city",
        "hotel_country",
        "hotel_number_of_guests",
        "hotel_total_cost",
        "id"
    ]


class CruiseListEncoder(ModelEncoder):
    model = Cruise
    properties = [
        "cruise_details",
        "cruise_line",
        "cruise_departure_city",
        "cruise_departure_date",
        "cruise_arrival_date",
        "cruise_number_of_passengers",
        "cruise_total_cost",
        "id"
    ]


class PackageListEncoder(ModelEncoder):
    model = Package
    properties = [
        "trip_name",
        "start_date",
        "end_date",
        "total_travelers",
        "package_total_cost",
        "id",
        "clients",
        "groups",
        "flights",
        "hotels",
        "cruises"

    ]

    def get_extra_data(self, o):
        extra_data = {}

        # Clients
        clients = o.clients.all()
        clients_id = []
        for client in clients:
            clients_id.append(client.id)
        extra_data["clients"] = clients_id

        # Groups
        groups = o.groups.all()
        groups_id = []
        for group in groups:
            groups_id.append(group.id)
        extra_data["groups"] = groups_id

        # Flights
        flights = o.flights.all()
        flights_id = []
        for flight in flights:
            flights_id.append(flight.id)
        extra_data["flights"] = flights_id

        # Hotels
        hotels = o.hotels.all()
        hotels_id = []
        for hotel in hotels:
            hotels_id.append(hotel.id)
        extra_data["hotels"] = hotels_id

        # Cruises
        cruises = o.cruises.all()
        cruises_id = []
        for cruise in cruises:
            cruises_id.append(cruise.id)
        extra_data["cruises"] = cruises_id

        return extra_data


class ClientGroupDetailEncoder(ModelEncoder):
    model = Client
    properties = [
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
        "id",
        "frequent_travel_group"  # Add the frequent_travel_group field
    ]
    encoders = {
        "frequent_travel_group": FrequentTravelGroupEncoder(),
    }


class ClientDetailEncoder(ModelEncoder):
    model = Client
    properties = [
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
        "id",
    ]



@require_http_methods(["GET", "POST"])
def frequent_travel_group_list(request):
    if request.method == "GET":
        frequent_travel_groups = FrequentTravelGroup.objects.all()
        return JsonResponse(
            {"frequent_travel_groups": frequent_travel_groups},
            encoder=FrequentTravelGroupEncoder
        )
    else:
        content = json.loads(request.body)
        frequent_travel_group = FrequentTravelGroup.objects.create(**content)
        return JsonResponse(
            frequent_travel_group,
            encoder=FrequentTravelGroupEncoder,
            safe=False
        )


@require_http_methods(["DELETE", "GET", "PUT"])
def frequent_travel_group_detail(request, id):
    if request.method == "GET":
        frequent_travel_groups = FrequentTravelGroup.objects.get(id=id)
        return JsonResponse(
            frequent_travel_groups,
            encoder=FrequentTravelGroupEncoder,
            safe=False,
        )
    elif request.method == "DELETE":
        count, _ = FrequentTravelGroup.objects.filter(id=id).delete()
        return JsonResponse({"deleted": count > 0})
    else:
        content = json.loads(request.body)
        FrequentTravelGroup.objects.filter(id=id).update(**content)
        frequent_travel_group = FrequentTravelGroup.objects.get(id=id)
        return JsonResponse(
            frequent_travel_group,
            encoder=FrequentTravelGroupEncoder,
            safe=False
        )


@require_http_methods(["GET", "POST"])
def client_list(request):
    if request.method == "GET":
        clients = Client.objects.all()
        return JsonResponse(
            {"clients": clients},
            encoder=ClientListEncoder
        )
    else:
        content = json.loads(request.body)
        frequent_travel_group_id = content.get("frequent_travel_group")

        if frequent_travel_group_id:
            try:
                frequent_travel_group = FrequentTravelGroup.objects.get(
                    id=frequent_travel_group_id
                    )
                content["frequent_travel_group"] = frequent_travel_group
            except FrequentTravelGroup.DoesNotExist:
                return JsonResponse(
                    {"message": "invalid frequent travel group id"},
                    status=400,
                )
        else:
            content.pop("frequent_travel_group", None)

        client = Client.objects.create(**content)
        return JsonResponse(
            {"client": client},
            encoder=ClientListEncoder,
            safe=False
        )


@require_http_methods(["DELETE", "GET", "PUT"])
def client_detail(request, id):
    if request.method == "GET":
        try:
            client = Client.objects.get(id=id)
            if client.frequent_travel_group:
                return JsonResponse(
                    client,
                    encoder=ClientGroupDetailEncoder,
                    safe=False
                    )
            else:
                return JsonResponse(
                    client,
                    encoder=ClientDetailEncoder,
                    safe=False
                    )
        except Client.DoesNotExist:
            return JsonResponse({"ERROR": "Client not found"}, status=404)
        else:
            try:
                client = Client.objects.get(id=id)
            except Client.DoesNotExist:
                return JsonResponse(
                    {"ERROR": "Client not found"},
                    status=404
                )
            return JsonResponse(
                client,
                encoder=ClientGroupDetailEncoder,
                safe=False
            )
    elif request.method == "DELETE":
        count, _ = Client.objects.filter(id=id).delete()
        return JsonResponse({"deleted": count > 0})
    else:
        content = json.loads(request.body)
        Client.objects.filter(id=id).update(**content)
        client = Client.objects.get(id=id)
        return JsonResponse(
            client,
            encoder=ClientDetailEncoder,
            safe=False
        )


@require_http_methods(["GET", "POST"])
def flight_list(request):
    if request.method == "GET":
        flights = Flight.objects.all()
        return JsonResponse(
            {"flights": flights},
            encoder=FlightListEncoder
        )
    else:
        content = json.loads(request.body)
        flight = Flight.objects.create(**content)
        return JsonResponse(
            flight,
            encoder=FlightListEncoder,
            safe=False
        )



@require_http_methods(["DELETE", "GET", "PUT"])
def flight_detail(request, id):
    if request.method == "GET":
        flights = Flight.objects.get(id=id)
        return JsonResponse(
            flights,
            encoder=FlightListEncoder,
            safe=False,
        )
    elif request.method == "DELETE":
        count, _ = Flight.objects.filter(id=id).delete()
        return JsonResponse({"deleted": count > 0})
    else:
        content = json.loads(request.body)
        Flight.objects.filter(id=id).update(**content)
        flight = Flight.objects.get(id=id)
        return JsonResponse(
            flight,
            encoder=FlightListEncoder,
            safe=False
        )


@require_http_methods(["GET", "POST"])
def hotel_list(request):
    if request.method == "GET":
        hotels = Hotel.objects.all()
        return JsonResponse(
            {"hotels": hotels},
            encoder=HotelListEncoder
        )
    else:
        content = json.loads(request.body)
        hotel = Hotel.objects.create(**content)
        return JsonResponse(
            hotel,
            encoder=HotelListEncoder,
            safe=False
        )


@require_http_methods(["DELETE", "GET", "PUT"])
def hotel_detail(request, id):
    if request.method == "GET":
        hotels = Hotel.objects.get(id=id)
        return JsonResponse(
            hotels,
            encoder=HotelListEncoder,
            safe=False
        )
    elif request.method == "DELETE":
        count, _ = Hotel.objects.get(id=id).delete()
        return JsonResponse({"deleted": count > 0})
    else:
        content = json.loads(request.body)
        Hotel.objects.filter(id=id).update(**content)
        hotel = Hotel.objects.get(id=id)
        return JsonResponse(
            hotel,
            encoder=HotelListEncoder,
            safe=False
        )


@require_http_methods(["GET", "POST"])
def cruise_list(request):
    if request.method == "GET":
        cruises = Cruise.objects.all()
        return JsonResponse(
            {"cruises": cruises},
            encoder=CruiseListEncoder
        )
    else:
        content = json.loads(request.body)
        cruise = Cruise.objects.create(**content)
        return JsonResponse(
            cruise,
            encoder=CruiseListEncoder,
            safe=False
        )


@require_http_methods(["DELETE", "GET", "PUT"])
def cruise_detail(request, id):
    if request.method == "GET":
        cruises = Cruise.objects.get(id=id)
        return JsonResponse(
            cruises,
            encoder=CruiseListEncoder,
            safe=False
        )
    elif request.method == "DELETE":
        count, _ = Cruise.objects.filter(id=id).delete()
        return JsonResponse({"deleted": count > 0})
    else:
        content = json.loads(request.body)
        Cruise.objects.filter(id=id).update(**content)
        cruise = Cruise.objects.get(id=id)
        return JsonResponse(
            cruise,
            encoder=CruiseListEncoder,
            safe=False
        )


@require_http_methods(["GET", "POST"])
def package_list(request):
    if request.method == "GET":
        packages = Package.objects.all()
        return JsonResponse(
            {"packages": packages},
            encoder=PackageListEncoder
        )
    else:
        content = json.loads(request.body)

        clients = content.pop("clients", [])
        groups = content.pop("groups", [])
        flights = content.pop("flights", [])
        hotels = content.pop("hotels", [])
        cruises = content.pop("cruises", [])

        package = Package.objects.create(**content)

        package.clients.set(clients)
        package.groups.set(groups)
        package.flights.set(flights)
        package.hotels.set(hotels)
        package.cruises.set(cruises)

        return JsonResponse(
            package,
            encoder=PackageListEncoder,
            safe=False
        )


@require_http_methods(["DELETE", "GET", "PUT"])
def package_detail(request, id):
    packages = Package.objects.get(id=id)
    if request.method == "GET":
        return JsonResponse(
            packages,
            encoder=PackageListEncoder,
            safe=False,
        )
    elif request.method == "DELETE":
        count, _ = Package.objects.filter(id=id).delete()
        return JsonResponse({"deleted": count > 0})
    else:
        content = json.loads(request.body)

        clients = content.pop("clients", [])
        groups = content.pop("groups", [])
        flights = content.pop("flights", [])
        hotels = content.pop("hotels", [])
        cruises = content.pop("cruises", [])

        packages.trip_name = content.get("trip_name", packages.trip_name)
        packages.start_date = content.get("start_date", packages.start_date)
        packages.end_date = content.get("end_date", packages.end_date)
        packages.total_travelers = content.get(
            "total_travelers", packages.total_travelers
            )
        packages.package_total_cost = content.get(
            "package_total_cost", packages.package_total_cost
            )
        packages.save()

        packages.clients.set(clients)
        packages.groups.set(groups)
        packages.flights.set(flights)
        packages.hotels.set(hotels)
        packages.cruises.set(cruises)

        packages = Package.objects.get(id=id)
        return JsonResponse(
            packages,
            encoder=PackageListEncoder,
            safe=False
        )
