from django.conf import settings
from django.db import models

NULLABLE = {"blank": True, "null": True}


class Course(models.Model):
    title = models.CharField(max_length=100, verbose_name="название")
    image = models.ImageField(upload_to="materials/", verbose_name="превью", **NULLABLE)
    description = models.CharField(max_length=100, verbose_name="описание", **NULLABLE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Lesson(models.Model):
    title = models.CharField(max_length=100, verbose_name="название")
    image = models.ImageField(upload_to="materials/", verbose_name="превью", **NULLABLE)
    description = models.TextField(verbose_name="описание", **NULLABLE)
    video_url = models.URLField(verbose_name="ссылка на видео", **NULLABLE)
    course = models.ForeignKey(
        Course,
        max_length=100,
        on_delete=models.CASCADE,
        verbose_name="урок",
        **NULLABLE
    )
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)


class Subscribe(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name="Пользователь",
                             **NULLABLE)
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, verbose_name="Курс", **NULLABLE
    )
    is_active = models.BooleanField(default=False, verbose_name='Статус подписки')

    def __str__(self):
        return f"{self.user}, {self.course}"

    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"