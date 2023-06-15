
from django.urls import path
from file_storage.views import FileListCreateView, FileRetrieveUpdateDeleteView

urlpatterns = [
    path('files/', FileListCreateView.as_view(), name='file-list-create'),
    path('files/<int:pk>/', FileRetrieveUpdateDeleteView.as_view(), name='file-retrieve-update-delete'),
]
