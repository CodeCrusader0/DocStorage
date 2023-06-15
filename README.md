# DocStorage
This is a simple file storage API service that allows users to manage binary files with versioning support. The API is built using Django and Django REST Framework.



## API Endpoints and Payloads

- **Create a File**
  - Endpoint: `/files/`
  - Method: `POST`
  - Payload:
    - `name`: Name of the file (string)
    - `version`: Version of the file (integer)
    - `file_data`: Binary data of the file (multipart/form-data)
   
- **Retrieve, Update, Delete a File**
  - Endpoint: `/files/<file_id>/`
  - Method: `GET`, `PUT`, `DELETE`
  - Payload:
    - `name`: Name of the file (string)
    - `version`: Version of the file (integer)
    - `file_data`: Binary data of the file (multipart/form-data)
   
  **List all Files**
  - Endpoint: `/files/`
  - Method: `GET`
 
  - ## Instructions

    To run and use the File Storage API, follow these steps:

  1. Clone the repository: git clone <>
  2. Install the dependencies: pip install -r requirements.txt
  3. Apply database migrations: python manage.py migrate
  4. Start the development server: python manage.py runserver
  5. The API will be accessible at `http://localhost:8000/`.
  6. Use a tool like cURL, Postman, or any other HTTP client to interact with the API endpoints as described above.

