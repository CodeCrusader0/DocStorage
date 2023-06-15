from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from file_storage.models import File


class FileAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.list_url = reverse('file-list-create')
        self.detail_url = reverse('file-retrieve-update-delete')
        self.file_data = b'Sample file data'

    def test_create_file(self):
        data = {
            'name': 'test_file.txt',
            'version': 1,
            'file_data': self.file_data,
        }
        response = self.client.post(self.list_url, data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(File.objects.count(), 1)

    def test_update_file(self):
        file = File.objects.create(name='test_file.txt', version=1, file_data=self.file_data)
        data = {
            'name': 'updated_file.txt',
            'version': 2,
            'file_data': self.file_data,
        }
        update_url = reverse('file-retrieve-update-delete', kwargs={'pk': file.pk})
        response = self.client.put(update_url, data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        file.refresh_from_db()
        self.assertEqual(file.name, 'updated_file.txt')
        self.assertEqual(file.version, 2)

    def test_delete_file(self):
        file = File.objects.create(name='test_file.txt', version=1, file_data=self.file_data)
        delete_url = reverse('file-retrieve-update-delete', kwargs={'pk': file.pk})
        response = self.client.delete(delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(File.objects.count(), 0)

    def test_list_files(self):
        File.objects.create(name='file1.txt', version=1, file_data=self.file_data)
        File.objects.create(name='file2.txt', version=1, file_data=self.file_data)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        
        file1_data = response.data[0]
        self.assertEqual(file1_data['name'], 'file1.txt')
        self.assertEqual(file1_data['version'], 1)
        
        file2_data = response.data[1]
        self.assertEqual(file2_data['name'], 'file2.txt')
        self.assertEqual(file2_data['version'], 1)
    
   

