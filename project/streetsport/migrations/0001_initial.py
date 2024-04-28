# Generated by Django 4.2.9 on 2024-04-09 14:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Game",
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
                    "title",
                    models.CharField(
                        help_text="title_field_help",
                        max_length=50,
                        unique=True,
                        verbose_name="title",
                    ),
                ),
                (
                    "normalize_title",
                    models.CharField(
                        editable=False,
                        help_text="normalize_title_field_help",
                        max_length=50,
                        verbose_name="normalize_title",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Team",
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
                    "title",
                    models.CharField(
                        help_text="title_field_help",
                        max_length=50,
                        unique=True,
                        verbose_name="title",
                    ),
                ),
                (
                    "normalize_title",
                    models.CharField(
                        editable=False,
                        help_text="normalize_title_field_help",
                        max_length=50,
                        verbose_name="normalize_title",
                    ),
                ),
                (
                    "rating",
                    models.PositiveIntegerField(
                        default=0,
                        help_text="rating_field_help",
                        verbose_name="rating",
                    ),
                ),
                (
                    "game",
                    models.ForeignKey(
                        blank=True,
                        help_text="game_field_help",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="teams",
                        related_query_name="teams",
                        to="streetsport.game",
                        verbose_name="game",
                    ),
                ),
                (
                    "lead",
                    models.ForeignKey(
                        blank=True,
                        help_text="lead_field_help",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="lead_teams",
                        related_query_name="lead_teams",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="lead",
                    ),
                ),
                (
                    "teammates",
                    models.ManyToManyField(
                        blank=True,
                        help_text="teammates_field_help",
                        related_name="teams",
                        related_query_name="teams",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="teammates",
                    ),
                ),
            ],
            options={
                "verbose_name": "team",
                "verbose_name_plural": "teams",
            },
        ),
        migrations.CreateModel(
            name="Order",
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
                    "description",
                    models.TextField(
                        blank=True,
                        help_text="description_field_help",
                        max_length=4000,
                        null=True,
                        verbose_name="description",
                    ),
                ),
                (
                    "location",
                    models.URLField(
                        blank=True,
                        help_text="location_field_help",
                        max_length=255,
                        null=True,
                        verbose_name="location",
                    ),
                ),
                (
                    "team_one",
                    models.ForeignKey(
                        help_text="team_one_field_help",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="orders_one",
                        related_query_name="orders_one",
                        to="streetsport.team",
                        verbose_name="team_one",
                    ),
                ),
                (
                    "team_two",
                    models.ForeignKey(
                        help_text="team_one_field_help",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="orders_two",
                        related_query_name="orders_two",
                        to="streetsport.team",
                        verbose_name="team_one",
                    ),
                ),
            ],
        ),
    ]