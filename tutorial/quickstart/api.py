from rest_framework import viewsets
from .serializers import UserSerializer
from .models import UserCustom

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = UserCustom.objects.all()
    serializer_class = UserSerializer
