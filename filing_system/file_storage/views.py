from rest_framework import generics
from file_storage.models import File
from file_storage.serializers import FileSerializer

class FileListCreateView(generics.ListCreateAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer

class FileRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer
