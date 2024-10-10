from django.urls import path, include
from rest_framework import routers
from project.views.project_viewset import ProjectViewSet
from project.views.task_viewset import TaskViewSet
from project.views.deliverable_viewset import DeliverableViewSet

router = routers.DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'deliverables', DeliverableViewSet)

urlpatterns = [
     path('', include(router.urls)),
]
