from rest_framework import viewsets, permissions, routers, serializers


from .models import Drink


class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = ['id', 'name', 'description', 'rating']


class DrinksViewSet(viewsets.ModelViewSet):
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer

    permission_classes = [permissions.IsAuthenticated]


def get_router_urls():
    router = routers.DefaultRouter()
    router.register('drinks', DrinksViewSet)

    return router.urls
