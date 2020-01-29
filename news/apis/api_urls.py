from django.urls import path
from news.apis.api_views import CategoryListAPIView, NewsListAPIView, NewsRetriveAPIView

# urls
urlpatterns = [
    path("categories/", CategoryListAPIView.as_view(), name="list_category"),
    path("list/", NewsListAPIView.as_view(), name="list_news"),
    path("list/<pk>/", NewsRetriveAPIView.as_view()),
]