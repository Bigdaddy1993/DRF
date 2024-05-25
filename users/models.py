from django.contrib.auth.models import AbstractUser
from django.db import models

from materials.models import Course, Lesson

NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    username = None
    email = models.EmailField(
        unique=True, verbose_name="Почта", help_text="Укажите почту"
    )

    avatar = models.ImageField(
        upload_to="users/", verbose_name="изображение", **NULLABLE
    )
    phone = models.CharField(max_length=35, verbose_name="телефон", **NULLABLE)
    city = models.CharField(max_length=30, verbose_name="город", **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"


# пользователь,
# дата оплаты,
# оплаченный курс или урок,
# сумма оплаты,
# способ оплаты: наличные или перевод на счет.


class Payment(models.Model):
    PAYMENT_METHOD_CHOICES = [("cash", "наличные"), ("card", "банковский перевод")]

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Пользователь"
    )
    date = models.DateTimeField(auto_now=True, verbose_name="дата оплаты")
    payment_course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        verbose_name="оплаченный курс",
        null=True,
        blank=True,
    )
    payment_lesson = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE,
        verbose_name="оплаченный урок",
        null=True,
        blank=True,
    )
    amount = models.PositiveIntegerField(verbose_name="сумма оплаты")
    payment_method = models.CharField(
        max_length=50,
        choices=PAYMENT_METHOD_CHOICES,
        default="card",
        verbose_name="Способ оплаты",
    )
    session_id = models.CharField(max_length=255, verbose_name="id сессии", **NULLABLE)
    link = models.URLField(max_length=400, verbose_name="ссылка на оплату", **NULLABLE)

    class Meta:
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"

    def __str__(self):
        return self.amount
