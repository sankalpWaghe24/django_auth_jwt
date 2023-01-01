# Generated by Django 4.1.4 on 2023-01-01 14:12

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="profile",
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
                (
                    "name",
                    models.CharField(
                        choices=[
                            ("Thumbnail (200x300)", "Thumbnail (200x300)"),
                            ("Medium(500x500)", "Medium(500x500)"),
                            ("Large (1024x768)", "Large (1024x768)"),
                            ("Grayscale", "Grayscale"),
                        ],
                        max_length=200,
                    ),
                ),
                (
                    "picture",
                    models.ImageField(
                        blank=True, upload_to=users.models.profile.nameFile
                    ),
                ),
            ],
        ),
    ]
