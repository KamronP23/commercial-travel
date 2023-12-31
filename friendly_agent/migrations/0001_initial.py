# Generated by Django 4.2.4 on 2023-08-05 16:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Client",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=50)),
                ("middle_name", models.CharField(blank=True, max_length=50, null=True)),
                ("last_name", models.CharField(max_length=50)),
                ("dob", models.DateField()),
                ("email", models.CharField(max_length=50)),
                ("street", models.CharField(max_length=50)),
                ("city", models.CharField(max_length=50)),
                ("zipcode", models.CharField(max_length=5)),
                ("state", models.CharField(max_length=50)),
                ("home_phone", models.CharField(max_length=12)),
                ("cell_phone", models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name="Cruise",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("cruise_details", models.CharField(max_length=50)),
                ("cruise_line", models.CharField(max_length=50)),
                ("cruise_departure_city", models.CharField(max_length=50)),
                ("cruise_departure_date", models.DateField()),
                ("cruise_arrival_date", models.DateField()),
                ("cruise_number_of_passengers", models.SmallIntegerField()),
                ("cruise_total_cost", models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Flight",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("flight_details", models.CharField(max_length=50)),
                ("airline", models.CharField(max_length=50)),
                ("departure_city", models.CharField(max_length=50)),
                ("departure_airport", models.CharField(max_length=10)),
                ("arrival_city", models.CharField(max_length=50)),
                ("arrival_airport", models.CharField(max_length=10)),
                ("layover", models.CharField(blank=True, max_length=50, null=True)),
                ("departure_time", models.DateTimeField()),
                ("arrival_time", models.DateTimeField()),
                ("flight_number_of_travelers", models.SmallIntegerField()),
                ("flight_total_cost", models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="FrequentTravelGroup",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("group_name", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Hotel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("hotel_details", models.CharField(max_length=50)),
                ("hotel_name", models.CharField(max_length=50)),
                ("check_in_date", models.DateField()),
                ("check_out_date", models.DateField()),
                ("hotel_city", models.CharField(max_length=50)),
                ("hotel_country", models.CharField(max_length=50)),
                ("hotel_number_of_guests", models.SmallIntegerField()),
                ("hotel_total_cost", models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Package",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("trip_name", models.CharField(max_length=50)),
                ("start_date", models.DateField()),
                ("end_date", models.DateField()),
                ("total_travelers", models.SmallIntegerField()),
                ("package_total_cost", models.SmallIntegerField()),
                (
                    "clients",
                    models.ManyToManyField(
                        blank=True, related_name="trips", to="friendly_agent.client"
                    ),
                ),
                (
                    "cruises",
                    models.ManyToManyField(
                        blank=True, related_name="trips", to="friendly_agent.cruise"
                    ),
                ),
                (
                    "flights",
                    models.ManyToManyField(
                        blank=True, related_name="trips", to="friendly_agent.flight"
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        related_name="trips",
                        to="friendly_agent.frequenttravelgroup",
                    ),
                ),
                (
                    "hotels",
                    models.ManyToManyField(
                        blank=True, related_name="trips", to="friendly_agent.hotel"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="client",
            name="frequent_travel_group",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="frequent_travel_group",
                to="friendly_agent.frequenttravelgroup",
            ),
        ),
    ]
