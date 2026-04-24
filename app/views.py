from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from .models import Item, Advertisement
from .serializers import ItemSerializer, AdvertisementSerializer


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class AdvertisementViewSet(viewsets.ModelViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    permission_classes = [IsAdminUser]

    def perform_create(self, serializer):   
        serializer.save(created_by=self.request.user)