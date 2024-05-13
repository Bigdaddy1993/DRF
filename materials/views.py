from rest_framework import viewsets
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
)

from materials.models import Course, Lesson
from materials.serializers import CourseSerializer, LessonSerializer
from rest_framework.permissions import IsAuthenticated

from users.permissions import IsModerator, IsOwner


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = serializer.save()
        user.owner = self.request.user
        user.save()

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [IsAuthenticated, ~IsModerator]
        elif self.action == 'destroy':
            permission_classes = [IsAuthenticated, IsOwner]
        elif self.action == 'list' or self.action == 'retrieve':
            permission_classes = [IsAuthenticated]
        elif self.action == 'update':
            permission_classes = [IsAuthenticated, IsModerator | IsOwner]

        return [permission() for permission in permission_classes]

    def get_queryset(self):
        if not self.request.user.groups.filter(name='moderator'):
            return Course.objects.filter(owner=self.request.user)
        elif self.request.user.groups.filter(name='moderator'):
            return Course.objects.all()


class LessonCreateApiView(CreateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, ~IsModerator]

    def perform_create(self, serializer):
        user = serializer.save()
        user.owner = self.request.user
        user.save()


class LessonListApiView(ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]


class LessonRetrieveApiView(RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class LessonUpdateApiView(UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModerator | IsOwner]


class LessonDestroyApiView(DestroyAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]
