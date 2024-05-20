from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from materials.models import Course, Lesson
from users.models import User


class SubscribeTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            email="test@mail.ru",
            is_staff=True,
            is_active=True,
            is_superuser=True,
            password=12345
        )
        self.client.force_authenticate(user=self.user)

        self.course = Course.objects.create(
            title="course 1", description="testing", owner=self.user
        )

    def test_subscribe_to_course(self):
        data = {
            "user": self.user.id,
            "course": self.course.id,
        }

        url = reverse("materials:subscribe_create")
        response = self.client.post(url, data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.json(),  {'message': 'Подписка добавлена'})


class LessonTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            email="test@mail.ru",
            is_staff=True,
            is_active=True,
            is_superuser=True,
            password=12345
        )
        self.client.force_authenticate(user=self.user)

        self.lesson = Lesson.objects.create(title="lesson 1", description="testing", owner=self.user)

    def test_get_create_lesson(self):
        data = {
            "title": "test11",
            "description": "test11",
            "video_url": "https://www.youtube.com/",
        }

        url = reverse("materials:create")
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_list_lesson(self):
        url = reverse("materials:list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_update_lesson(self):
        data = {
            "title": "test5",
            "description": "test5"
        }
        url = reverse("materials:update", args=(self.lesson.pk,))
        response = self.client.patch(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_delete_lesson(self):
        url = reverse("materials:delete", args=(self.lesson.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_get_retrieve_lesson(self):
        url = reverse("materials:retrieve", args=(self.lesson.pk,))
        response = self.client.get(url)
        # data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
