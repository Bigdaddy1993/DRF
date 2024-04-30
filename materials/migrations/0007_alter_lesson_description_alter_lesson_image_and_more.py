# Generated by Django 5.0.4 on 2024-04-30 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("materials", "0006_alter_course_description_alter_course_image_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lesson",
            name="description",
            field=models.TextField(blank=True, null=True, verbose_name="описание"),
        ),
        migrations.AlterField(
            model_name="lesson",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to="materials/", verbose_name="превью"
            ),
        ),
        migrations.AlterField(
            model_name="lesson",
            name="video_url",
            field=models.URLField(
                blank=True, null=True, verbose_name="ссылка на видео"
            ),
        ),
    ]
