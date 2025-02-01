# FAQ-App
This project is a Django-based FAQ management system that supports multiple languages (English, Hindi, and Bengali).
# Features
- Multi-Language Support for FAQs (English, Hindi, Bengali).
- WYSIWYG Editor for rich-text formatting in FAQ answers.
- CRUD Operations for managing FAQs via the admin interface.
- API Integration for fetching FAQs in different languages.
# Installation Steps
Follow the instructions below to get your development environment set up.

**Prerequisites**
Ensure that you have the following installed on your machine:

- Python 3.8 or higher
- pip (Python package installer)
- Django 3.0 or higher
  
**Clone the Repository**
```python
bash
git clone https://github.com/your-username/faq-management-system.git
cd faq-management-system
```
**Set Up a Virtual Environment**
It's recommended to use a virtual environment to avoid conflicts with system-wide Python packages.

```python
bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

**Install Dependencies**
Install all the required packages from `requirements.txt`.

```python
bash
pip install -r requirements.txt
```

**Set Up the Database**
Run the following commands to set up your database:

- Apply the migrations:

```python
bash
python manage.py migrate
```
- Create a superuser to manage the admin panel:

```python
bash
python manage.py createsuperuser
```

-Start the Django development server:

```python
bash
python manage.py runserver
```

**Access the Application**
Once the server is running, open your browser and go to:
```python
cpp
http://127.0.0.1:8000/
```
To access the Django admin panel, go to:

```python
arduino
http://127.0.0.1:8000/admin/
```
Login using the superuser credentials you created.

# API Usage Examples
The system provides a simple API to fetch FAQs based on the selected language.

**Endpoints**
1. Get All FAQs

URL: `/api/faqs/`

Method: `GET`

Query Parameters:

- `lang`: The language in which the FAQs are required. Supported values: `en`, `hi`, `bn`. Defaults to `en`.
Example Request:

```python
bash
curl -X GET "http://127.0.0.1:8000/api/faqs/?lang=hi"
```
Example Response:

```json
json
{
    "faqs": [
        {
            "id": 1,
            "question": "Django क्या है?",
            "answer": "Django एक वेब फ्रेमवर्क है।"
        },
        {
            "id": 2,
            "question": "Django का इस्तेमाल क्यों करें?",
            "answer": "Django बहुत ही शक्तिशाली और सुरक्षित वेब फ्रेमवर्क है।"
        }
    ]
}
```
2. Get a Single FAQ

URL: `/api/faqs/{faq_id}/`

Method: `GET`

Example Request:

```python
bash
curl -X GET "http://127.0.0.1:8000/api/faqs/1/"
```
Example Response:

```json
json
{
    "id": 1,
    "question_en": "What is Django?",
    "answer_en": "Django is a web framework.",
    "question_hi": "Django क्या है?",
    "answer_hi": "Django एक वेब फ्रेमवर्क है।",
    "question_bn": "Django কি?",
    "answer_bn": "Django একটি ওয়েব ফ্রেমওয়ার্ক।"
}
```
