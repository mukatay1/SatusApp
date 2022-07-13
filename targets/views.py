from rest_framework import generics

from .serializers import TargetsSerializer
from .models import Targets


class TargetsView(generics.ListCreateAPIView):
    serializer_class = TargetsSerializer
    queryset = Targets.objects.all()
