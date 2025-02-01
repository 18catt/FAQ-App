from django.urls import path
from .views import get_faqs, faq_list, add_faq

app_name = "faq_app"

urlpatterns = [
    path('api/faqs/', get_faqs, name='get_faqs'),
    path('', faq_list, name='faq_list'),
    path('add/', add_faq, name='add_faq'),
]

