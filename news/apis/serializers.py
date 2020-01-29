from rest_framework import serializers
from news.models import Category, News


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "id", "title"


class NewsSerializer(serializers.ModelSerializer):
    category = CategoryListSerializer(many=True)

    class Meta:
        model = News
        fields = "id", "title", "content", "cover_image", "author", "category", "created_at"