from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, SkillViewSet


router = DefaultRouter()
router.register(r"projects", ProjectViewSet, basename="projects")
router.register(r"skills", SkillViewSet, basename="skills")

urlpatterns = [
    path("", include(router.urls))
]