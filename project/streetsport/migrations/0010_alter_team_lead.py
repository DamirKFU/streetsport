# Generated by Django 4.2.9 on 2024-04-21 15:32

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("streetsport", "0009_alter_team_lead"),
    ]

    operations = [
        migrations.AlterField(
            model_name="team",
            name="lead",
            field=models.OneToOneField(
                blank=True,
                help_text="lead_field_help",
                null=True,
                on_delete=models.SET_NULL,
                related_name="lead_teams",
                related_query_name="lead_teams",
                to=settings.AUTH_USER_MODEL,
                verbose_name="lead",
            ),
        ),
    ]
