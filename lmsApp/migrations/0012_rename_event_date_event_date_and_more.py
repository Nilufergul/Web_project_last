# Generated by Django 4.2.13 on 2024-05-28 23:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("lmsApp", "0011_event"),
    ]

    operations = [
        migrations.RenameField(
            model_name="event",
            old_name="event_date",
            new_name="date",
        ),
        migrations.RemoveField(
            model_name="event",
            name="event_theme",
        ),
        migrations.RemoveField(
            model_name="event",
            name="event_title",
        ),
        migrations.AddField(
            model_name="event",
            name="theme",
            field=models.CharField(default="Default Theme", max_length=50),
        ),
        migrations.AddField(
            model_name="event",
            name="title",
            field=models.CharField(default="Default Title", max_length=200),
        ),
    ]
