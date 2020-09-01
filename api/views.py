from rest_framework import viewsets
from .serializers import UserSerializer, GlossarySerializer
# from django.contrib.auth.models import User
from rest_framework import permissions
from glossary.models import Glossary


class PostView(viewsets.ModelViewSet):
    queryset = Glossary.objects.all()
    # queryset = Glossary.objects.filter(account=request.user).get(word=w)
    # serializer_class = UserSerializer
    # queryset = User.objects.all()
    serializer_class = GlossarySerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
