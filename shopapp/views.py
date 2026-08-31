from .serializers import ItemSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Item


class ItemPage(ModelViewSet):
    queryset = Item.objects.all().order_by('id')
    serializer_class = ItemSerializer


class ItemEdit(APIView):
    def put(self, req, *args, **kwargs):
        item = Item.objects.filter(slug=kwargs["slug"]).first()

        if not item:
            return Response(
                {"error": "Товар не знайдено"},
                status=status.HTTP_404_NOT_FOUND
            )
        item.image = req.data.get("image")
        item.title = req.data.get("title")
        item.price = req.data.get("price")
        item.desc = req.data.get("desc")

        item.save()

        return Response(
            {"message": "Товар успішно оновлено"},
            status=status.HTTP_200_OK
        )