from .serialisers import ArticlesSerializer
from .models import Articles
from rest_framework import permissions, viewsets


class ArticlesViewSets(viewsets.ModelViewSet):
    queryset = Articles.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ArticlesSerializer
