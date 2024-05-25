from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView, get_object_or_404)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from materials.models import Course, Lesson, Subscribe
from materials.paginators import MaterialsPaginator
from materials.serializers import (CourseSerializer, LessonSerializer,
                                   SubscribeSerializer)
from users.permissions import IsModerator, IsOwner


class CourseViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Course, have permissions.
    """
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = MaterialsPaginator

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
    """
    generic for Create Lesson
    """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, ~IsModerator]

    def perform_create(self, serializer):
        user = serializer.save()
        user.owner = self.request.user
        user.save()


class LessonListApiView(ListAPIView):
    """
    generic for list Lesson
    """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = MaterialsPaginator


class LessonRetrieveApiView(RetrieveAPIView):
    """
       generic for Retrieve Lesson
       """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class LessonUpdateApiView(UpdateAPIView):
    """
       generic for Update Lesson
       """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModerator | IsOwner]


class LessonDestroyApiView(DestroyAPIView):
    """
       generic for Delete Lesson
       """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class SubscribeAPIView(CreateAPIView):
    """
    Create for Subscribe
    """
    serializer_class = SubscribeSerializer

    def post(self, *args, **kwargs):
        """
        Activate or Deactivate Subscribe
        """
        user = self.request.user
        course_id = self.request.data.get("course")
        course = get_object_or_404(Course, pk=course_id)
        subs_item = Subscribe.objects.all().filter(user=user).filter(course=course).first()

        if subs_item:
            subs_item.delete()
            message = 'Подписка удалена'
        else:
            Subscribe.objects.create(user=user, course=course)
            message = 'Подписка добавлена'

        return Response({"message": message})
