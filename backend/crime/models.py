from common.models import DataTransferObject
from django.db import models


class CrimeVO(models.Model):
    police = models.TextField()
    crime = models.TextField()
    create_at = models.DateTimeField()


class CrimeDTO(DataTransferObject):
    police = ''
    crime = ''
    create_at = ''

