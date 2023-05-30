from django.urls import path
from .views import PicListView, PicDetailView, PicCreateView, PicDeleteView

urlpatterns = [
	path('', PicListView.as_view(), name='pic'),
    path('<int:pk>/', PicDetailView.as_view(), name='foto'),
    path('add-foto/', PicCreateView.as_view(), name='add-foto'),
    path('<int:pk>/delete/', PicDeleteView.as_view(), name='pic-delete'),
]