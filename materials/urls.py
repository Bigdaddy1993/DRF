from django.urls import path
from rest_framework.routers import SimpleRouter

from materials.apps import MaterialsConfig
from materials.views import (CourseViewSet, LessonCreateApiView,
                             LessonDestroyApiView, LessonListApiView,
                             LessonRetrieveApiView, LessonUpdateApiView,
                             SubscribeAPIView)

app_name = MaterialsConfig.name

router = SimpleRouter()
router.register(r"materials", CourseViewSet, basename="materials")

urlpatterns = [
                  path("lesson/", LessonListApiView.as_view(), name="list"),
                  path("lesson/create/", LessonCreateApiView.as_view(), name="create"),
                  path("lesson/<int:pk>/", LessonRetrieveApiView.as_view(), name="retrieve"),
                  path("lesson/delete/<int:pk>/", LessonDestroyApiView.as_view(), name="delete"),
                  path("lesson/update/<int:pk>/", LessonUpdateApiView.as_view(), name="update"),

                  path("subscribe/", SubscribeAPIView.as_view(), name="subscribe_create"),
              ] + router.urls
