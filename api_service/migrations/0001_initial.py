# Generated by Django 4.2.1 on 2023-06-10 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Destination",
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
                ("name", models.TextField(blank=True, null=True)),
                ("art", models.IntegerField(blank=True, null=True)),
                ("entertainment", models.IntegerField(blank=True, null=True)),
                ("sightings", models.IntegerField(blank=True, null=True)),
                ("culinary", models.IntegerField(blank=True, null=True)),
                ("shopping", models.IntegerField(blank=True, null=True)),
                ("image_link", models.TextField(blank=True, null=True)),
                ("location", models.TextField(blank=True, null=True)),
                ("description", models.TextField(blank=True, null=True)),
                ("weekdays_time", models.TextField(blank=True, null=True)),
                ("weekend_time", models.TextField(blank=True, null=True)),
                (
                    "latitude",
                    models.DecimalField(
                        blank=True, decimal_places=7, max_digits=8, null=True
                    ),
                ),
                (
                    "longitude",
                    models.DecimalField(
                        blank=True, decimal_places=7, max_digits=10, null=True
                    ),
                ),
                ("lowest_price", models.IntegerField(blank=True, null=True)),
                ("highest_price", models.IntegerField(blank=True, null=True)),
                ("additional_price", models.IntegerField(blank=True, null=True)),
                ("column_1_star", models.IntegerField(blank=True, null=True)),
                ("column_2_star", models.IntegerField(blank=True, null=True)),
                ("column_3_star", models.IntegerField(blank=True, null=True)),
                ("column_4_star", models.IntegerField(blank=True, null=True)),
                ("column_5_star", models.IntegerField(blank=True, null=True)),
                ("total_reviews", models.IntegerField(blank=True, null=True)),
                (
                    "rating",
                    models.DecimalField(
                        blank=True, decimal_places=1, max_digits=2, null=True
                    ),
                ),
                ("location_link", models.TextField(blank=True, null=True)),
            ],
            options={
                "db_table": "destination",
                "managed": False,
            },
        ),
    ]
