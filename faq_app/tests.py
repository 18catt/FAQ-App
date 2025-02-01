from django.test import TestCase
from .models import FAQ

class FAQTestCase(TestCase):
    def setUp(self):
        # Create a single FAQ with the English question and answer
        FAQ.objects.create(
            question_en="What is Django?", 
            answer_en="Django is a web framework."
        )

    def test_translation(self):
        # Get the FAQ we created in the setup
        faq = FAQ.objects.get(question_en="What is Django?")

        # Check if the Hindi and Bengali translations are set
        self.assertIsNotNone(faq.question_hi)  # Ensure Hindi translation exists
        self.assertIsNotNone(faq.answer_hi)    # Ensure Hindi answer exists

        self.assertIsNotNone(faq.question_bn)  # Ensure Bengali translation exists
        self.assertIsNotNone(faq.answer_bn)    # Ensure Bengali answer exists

    def test_api_response(self):
        # Test API response for Hindi
        response_hi = self.client.get('/api/faqs/?lang=hi')
        
        # Ensure the status code is 200
        self.assertEqual(response_hi.status_code, 200)
        
        # Check if the content includes the Hindi translation of the FAQ
        self.assertIn("Django क्या है?", response_hi.content.decode())  # Check if Hindi question exists
        self.assertIn("Django एक वेब फ्रेमवर्क है।", response_hi.content.decode())  # Check if Hindi answer exists




