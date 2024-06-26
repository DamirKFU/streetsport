# Generated by Django 4.2.9 on 2024-03-11 19:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("feedback", "0010_alter_feedbackauthor_options_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="feedback",
            name="author",
        ),
        migrations.AddField(
            model_name="feedbackauthor",
            name="feedback",
            field=models.OneToOneField(
                default=1,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="author",
                related_query_name="author",
                to="feedback.feedback",
            ),
            preserve_default=False,
        ),
    ]
