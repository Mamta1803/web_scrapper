from django.urls import path
from news_app import views

urlpatterns = [
    path('sort_comments/', views.sort_comments, name='sort_comments'),
    path('karma_count/', views.karma_count, name='karma_count'),
]
