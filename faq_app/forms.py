from django import forms
from .models import FAQ
from ckeditor.widgets import CKEditorWidget

class FAQForm(forms.ModelForm):
    class Meta:
        model = FAQ
        fields = ['question_en', 'answer_en']

        widgets = {
            'answer_en': CKEditorWidget(),  # Using CKEditor for rich text editing
        }


