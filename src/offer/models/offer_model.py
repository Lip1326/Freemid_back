from django.db import models

from base.helpers.date_time_model import DateTimeModel
from user.models.client_model import ClientModel


class OfferModel(DateTimeModel):
    client = models.ForeignKey(ClientModel, on_delete=models.CASCADE, related_name='offers')
    title = models.CharField(max_length=255)
    description = models.TextField()
    required_skills = models.ManyToManyField('SkillModel', through='OfferSkillModel')
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    deadline = models.DateTimeField()
