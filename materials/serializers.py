from rest_framework import serializers

from materials.models import Course, Lesson, Subscribe
from materials.validators import UrlValidator


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"
        validators = [UrlValidator(field='video_url')]


# class CourseSerializer(serializers.ModelSerializer):
#     lesson_count = serializers.IntegerField(source='lesson_set.all.last.lesson', read_only=True)
#     lesson = LessonSerializer(source='lesson_set', many=True)
#
#     class Meta:
#         model = Course
#         fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()
    lesson = LessonSerializer(source='lesson_set', many=True, read_only=True)
    subscribe = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = "__all__"

    def get_lesson_count(self, instance):
        if Lesson.objects.filter(course=instance):
            return Lesson.objects.filter(course=instance).count()
        return 'нет уроков в этом курсе'

    def get_subscribe(self, instance):
        user = self.context.get("request").user
        return Subscribe.objects.all().filter(user=user).filter(course=instance).exists()


class SubscribeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscribe
        fields = "__all__"
