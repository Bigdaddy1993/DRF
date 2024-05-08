from rest_framework import serializers

from materials.models import Course, Lesson


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"


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

    class Meta:
        model = Course
        fields = "__all__"

    def get_lesson_count(self, instance):
        if Lesson.objects.filter(course=instance):
            return Lesson.objects.filter(course=instance).count()
        return 'нет уроков в этом курсе'
