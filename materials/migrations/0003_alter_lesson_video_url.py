# Generated by Django 5.0.4 on 2024-04-30 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("materials", "0002_alter_course_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lesson",
            name="video_url",
            field=models.URLField(verbose_name="ссылка на видео"),
        ),
    ]
