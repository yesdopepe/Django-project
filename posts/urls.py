from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('<int:pk>/delete/', views.delete_post, name='post_delete'),
]
