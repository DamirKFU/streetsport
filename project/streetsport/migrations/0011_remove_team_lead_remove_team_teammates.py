# Generated by Django 4.2.9 on 2024-04-21 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("streetsport", "0010_alter_team_lead"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="team",
            name="lead",
        ),
        migrations.RemoveField(
            model_name="team",
            name="teammates",
        ),
    ]