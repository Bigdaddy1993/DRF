from celery import shared_task
from django.core.mail import send_mail

from config import settings
from materials.models import Course, Subscribe


@shared_task
def send_update():
    course = Course.objects.all()
    sub = Subscribe.objects.all()
    for user in sub:
        send_mail(
            subject=f'{course.title}',
            message=f'Курс на который вы подписаны обновлен !)) {course.title}!',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[f'{user.user}'],
            fail_silently=True,
        )
