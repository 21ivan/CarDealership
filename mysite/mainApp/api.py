from .serialisers import CarSerializer, BrandSerializer
from .models import Car, Info, Brand
from rest_framework import permissions, viewsets


class CarViewSets(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CarSerializer


class BrandViewSets(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = BrandSerializer