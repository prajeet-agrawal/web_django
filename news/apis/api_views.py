from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from news.apis.serializers import CategoryListSerializer, NewsSerializer


class CategoryListAPIView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = CategoryListSerializer
    model = serializer_class.Meta.model
    queryset = model.objects.all()


class NewsListAPIView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = NewsSerializer
    model = serializer_class.Meta.model
    queryset = model.objects.all()


class NewsRetriveAPIView(RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = NewsSerializer
    model = serializer_class.Meta.model
    queryset = model.objects.all()