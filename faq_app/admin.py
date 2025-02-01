from django.contrib import admin
from .models import FAQ
from ckeditor.widgets import CKEditorWidget
from django import forms

# Custom form to use CKEditor widget in the admin
class FAQForm(forms.ModelForm):
    class Meta:
        model = FAQ
        fields = '__all__'
        widgets = {
            'answer_en': CKEditorWidget(),  #CKEditor for English answer
            'answer_hi': CKEditorWidget(),  #CKEditor for Hindi answer
            'answer_bn': CKEditorWidget(),  #CKEditor for Bengali answer
        }

# Custom admin class to use the custom form
@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    form = FAQForm  #Use the custom form with CKEditor widget
    list_display = ('question_en', 'answer_en', 'question_hi', 'answer_hi', 'question_bn', 'answer_bn')
    search_fields = ('question_en', 'question_hi', 'question_bn')  # Allows searching questions in all languages
    ordering = ('question_en',)  # Orders the FAQs based on English questions


