# Generated by Django 4.2.9 on 2024-04-16 04:56

from django.db import migrations
import sorl.thumbnail.fields
import streetsport.models


class Migration(migrations.Migration):

    dependencies = [
        ("streetsport", "0007_team_avatar"),
    ]

    operations = [
        migrations.AddField(
            model_name="game",
            name="icon",
            field=sorl.thumbnail.fields.ImageField(
                blank=True,
                help_text="game_icon_field_help",
                null=True,
                upload_to=streetsport.models.Game.get_path_image,
                verbose_name="game_icon",
            ),
        ),
    ]
