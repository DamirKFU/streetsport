# Generated by Django 4.2.9 on 2024-04-14 18:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import feedback.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("feedback", "0019_remove_feedbackauthor_name"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="feedback",
            options={
                "verbose_name": "feedback",
                "verbose_name_plural": "feedbacks",
            },
        ),
        migrations.AlterModelOptions(
            name="feedbackauthor",
            options={
                "verbose_name": "feedback_author",
                "verbose_name_plural": "feedback_authors",
            },
        ),
        migrations.AlterModelOptions(
            name="feedbackfile",
            options={
                "verbose_name": "feedback_file",
                "verbose_name_plural": "feedback_files",
            },
        ),
        migrations.AlterModelOptions(
            name="statuslog",
            options={
                "verbose_name": "status_log",
                "verbose_name_plural": "status_logs",
            },
        ),
        migrations.AlterField(
            model_name="feedback",
            name="created_on",
            field=models.DateTimeField(
                auto_now_add=True,
                help_text="created_field_help",
                null=True,
                verbose_name="created",
            ),
        ),
        migrations.AlterField(
            model_name="feedback",
            name="status",
            field=models.CharField(
                choices=[
                    ("NW", "new_status"),
                    ("PD", "pending_status"),
                    ("CP", "complete_status"),
                ],
                default="NW",
                help_text="status_field_help",
                max_length=2,
                verbose_name="status",
            ),
        ),
        migrations.AlterField(
            model_name="feedback",
            name="text",
            field=models.TextField(
                help_text="text_field_help",
                max_length=4000,
                verbose_name="text",
            ),
        ),
        migrations.AlterField(
            model_name="feedbackauthor",
            name="feedback",
            field=models.OneToOneField(
                help_text="feedback_field_help",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="author",
                related_query_name="author",
                to="feedback.feedback",
                verbose_name="feedback",
            ),
        ),
        migrations.AlterField(
            model_name="feedbackauthor",
            name="mail",
            field=models.EmailField(
                help_text="mail_field_help",
                max_length=254,
                verbose_name="адрес электронной почты",
            ),
        ),
        migrations.AlterField(
            model_name="feedbackfile",
            name="feedback",
            field=models.ForeignKey(
                help_text="feedback_field_help",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="files",
                related_query_name="files",
                to="feedback.feedback",
                verbose_name="feedback",
            ),
        ),
        migrations.AlterField(
            model_name="feedbackfile",
            name="file",
            field=models.FileField(
                help_text="file_field_help",
                upload_to=feedback.models.FeedbackFile.upload_to,
                verbose_name="file",
            ),
        ),
        migrations.AlterField(
            model_name="statuslog",
            name="feedback",
            field=models.ForeignKey(
                help_text="feedback_field_help",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="feedback.feedback",
                verbose_name="feedback",
            ),
        ),
        migrations.AlterField(
            model_name="statuslog",
            name="from_status",
            field=models.CharField(
                choices=[
                    ("NW", "new_status"),
                    ("PD", "pending_status"),
                    ("CP", "complete_status"),
                ],
                db_column="from",
                help_text="from_status_field_help",
                max_length=2,
                verbose_name="from_status",
            ),
        ),
        migrations.AlterField(
            model_name="statuslog",
            name="timestamp",
            field=models.DateTimeField(
                auto_now_add=True,
                help_text="timestamp_field_help",
                null=True,
                verbose_name="timestamp",
            ),
        ),
        migrations.AlterField(
            model_name="statuslog",
            name="to_status",
            field=models.CharField(
                choices=[
                    ("NW", "new_status"),
                    ("PD", "pending_status"),
                    ("CP", "complete_status"),
                ],
                db_column="to",
                help_text="to_status_field_help",
                max_length=2,
                verbose_name="to_status",
            ),
        ),
        migrations.AlterField(
            model_name="statuslog",
            name="user",
            field=models.ForeignKey(
                help_text="user_field_help",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
                verbose_name="пользователь",
            ),
        ),
    ]
