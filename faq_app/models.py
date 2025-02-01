from django.db import models
from ckeditor.fields import RichTextField
from googletrans import Translator

translator = Translator()

class FAQ(models.Model):
    question_en = models.TextField()
    answer_en = RichTextField()  # WYSIWYG editor
    question_hi = models.TextField(blank=True, null=True)
    answer_hi = RichTextField(blank=True, null=True)
    question_bn = models.TextField(blank=True, null=True)  
    answer_bn = RichTextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        # Avoid translating on every save if the translation exists
        if not self.question_hi or not self.answer_hi or not self.question_bn or not self.answer_bn:
            # Translate and save
            if not self.question_hi:
                self.question_hi = translator.translate(self.question_en, dest='hi').text
            if not self.answer_hi:
                self.answer_hi = translator.translate(self.answer_en, dest='hi').text
            if not self.question_bn:
                self.question_bn = translator.translate(self.question_en, dest='bn').text
            if not self.answer_bn:
                self.answer_bn = translator.translate(self.answer_en, dest='bn').text
        super(FAQ, self).save(*args, **kwargs)

    def get_question(self, lang='en'):
        return getattr(self, f'question_{lang}', self.question_en) or self.question_en

    def __str__(self):
        return self.question_en




