from django.urls import path

from .views import PostListView, PostDetailView, PostUpdateView, PostDeleteView, PostCreateView

urlpatterns = [
    path('lenta/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('lenta/post_new/', PostCreateView.as_view(), name='post_new'),
    path('lenta/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('lenta/<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('', PostListView.as_view(), name='home'),
]