# Generated by Django 5.0.4 on 2024-04-30 20:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Lesson",
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
                ("title", models.CharField(max_length=100, verbose_name="название")),
                (
                    "image",
                    models.ImageField(upload_to="materials/", verbose_name="превью"),
                ),
                ("description", models.TextField(verbose_name="описание")),
                ("video_url", models.TextField(verbose_name="ссылка на видео")),
            ],
        ),
        migrations.CreateModel(
            name="Course",
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
                ("title", models.CharField(max_length=100, verbose_name="название")),
                (
                    "image",
                    models.ImageField(upload_to="materials/", verbose_name="превью"),
                ),
                ("description", models.TextField(verbose_name="описание")),
                (
                    "lesson",
                    models.ForeignKey(
                        max_length=100,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="materials.lesson",
                        verbose_name="урок",
                    ),
                ),
            ],
            options={
                "verbose_name": "Курс",
                "verbose_name_plural": "Курсы",
            },
        ),
    ]
