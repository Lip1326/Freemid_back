from rest_framework import viewsets
from offer.models.offerskill_model import OfferSkillModel
from offer.serializers.offerskill_serializer import OfferSkillSerializer


class OfferSkillViewSet(viewsets.ModelViewSet):
    queryset = OfferSkillModel.objects.all()
    serializer_class = OfferSkillSerializer
