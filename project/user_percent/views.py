from rest_framework import viewsets

from user_percent.models import UserPercent
from user_percent.serializers import UserPercentSerializer


class UserPercentViewSet(viewsets.ModelViewSet):
    queryset = UserPercent.objects.all()
    serializer_class = UserPercentSerializer
