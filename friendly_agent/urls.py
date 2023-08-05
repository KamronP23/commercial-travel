from django.urls import path
from friendly_agent.views import (
    client_list,
    client_detail,
    frequent_travel_group_list,
    frequent_travel_group_detail,
    flight_list,
    flight_detail,
    hotel_list,
    hotel_detail,
    cruise_list,
    cruise_detail,
    package_list,
    package_detail
)

urlpatterns = [
    path("clients/", client_list, name="clients"),
    path("clients/<int:id>/", client_detail, name="clients_detail"),
    path(
        "travel_groups/",
        frequent_travel_group_list,
        name="travel_groups"
        ),
    path(
        "travel_groups/<int:id>/",
        frequent_travel_group_detail,
        name="travel_groups_detail"
        ),
    path("flights/", flight_list, name="flights"),
    path("flights/<int:id>/", flight_detail, name="flight_detail"),
    path("hotels/", hotel_list, name="hotels"),
    path("hotels/<int:id>/", hotel_detail, name="hotel_detail"),
    path("cruises/", cruise_list, name="cruises"),
    path("cruises/<int:id>/", cruise_detail, name="cruise_detail"),
    path("packages/", package_list, name="packages"),
    path("packages/<int:id>/", package_detail, name="package_detail")
]
