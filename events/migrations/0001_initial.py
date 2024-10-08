# Generated by Django 4.1.3 on 2024-09-11 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Event",
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
                ("title", models.CharField(max_length=255)),
                ("description", models.TextField()),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("wedding", "Wedding"),
                            ("party", "Party"),
                            ("club", "Club Event"),
                            ("government", "Government Event"),
                            ("conference", "Conference"),
                            ("other", "Other"),
                        ],
                        max_length=20,
                    ),
                ),
                ("date", models.DateField()),
                ("link", models.URLField()),
            ],
        ),
    ]
