from rest_framework import viewsets
from offer.models.skill_model import SkillModel
from offer.serializers.skill_serializer import SkillSerializer


class SkillViewSet(viewsets.ModelViewSet):
    queryset = SkillModel.objects.all()
    serializer_class = SkillSerializer
