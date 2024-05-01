from django.db import models

NULLABLE = {"blank": True, "null": True}


class Course(models.Model):
    title = models.CharField(max_length=100, verbose_name="название")
    image = models.ImageField(upload_to="materials/", verbose_name="превью", **NULLABLE)
    description = models.CharField(max_length=100, verbose_name="описание", **NULLABLE)

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Lesson(models.Model):
    title = models.CharField(max_length=100, verbose_name="название")
    image = models.ImageField(upload_to="materials/", verbose_name="превью", **NULLABLE)
    description = models.TextField(verbose_name="описание", **NULLABLE)
    video_url = models.URLField(verbose_name="ссылка на видео", **NULLABLE)
    lesson = models.ForeignKey(
        Course,
        max_length=100,
        on_delete=models.CASCADE,
        verbose_name="урок",
        **NULLABLE
    )
