from django.urls import path
from news import views

urlpatterns = [
    path("create/", views.NewsCreateView.as_view(), name="create_news"),
    path("update/<pk>", views.NewsUpdateView.as_view(), name="update_news"),
    path("delete/<pk>", views.NewsDeleteView.as_view(), name="delete_news"),
    path("<category_id>/", views.CategoryNewsView.as_view(), name="category_news"),
    path("<pk>/<slug>", views.NewsDetail.as_view(), name="single_news"),
    # comment
    #path("<category_id>/", views.comment.as_view(), name="comments"),
]

