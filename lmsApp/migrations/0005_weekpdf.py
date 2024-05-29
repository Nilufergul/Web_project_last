# Generated by Django 5.0.4 on 2024-05-27 17:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("lmsApp", "0004_lesson_student_alter_message_options_week_note"),
    ]

    operations = [
        migrations.CreateModel(
            name="WeekPDF",
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
                ("title", models.CharField(max_length=200)),
                ("pdf", models.FileField(upload_to="week_pdfs/")),
                (
                    "week",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="lmsApp.week"
                    ),
                ),
            ],
        ),
    ]
