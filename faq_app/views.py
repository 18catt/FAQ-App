from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.core.cache import cache
from .models import FAQ
from .forms import FAQForm

def get_translated_answer(faq, lang):
    """
    Retrieve the translated answer based on the selected language.
    
    Args:
        faq (FAQ): The FAQ object.
        lang (str): The language code ('en', 'hi', 'bn').

    Returns:
        str: The translated answer or fallback to English.
    """
    if lang == 'hi':
        return faq.answer_hi or faq.answer_en
    elif lang == 'bn':
        return faq.answer_bn or faq.answer_en
    return faq.answer_en


def get_faqs(request):
    """
    Retrieve FAQs from cache or the database, based on the selected language.
    
    Args:
        request: The HTTP request object.

    Returns:
        JsonResponse: A JSON response containing the FAQ data.
    """
    lang = request.GET.get('lang', 'en')
    cache_key = f'faqs_{lang}'
    
    faqs_data = cache.get(cache_key)
    if not faqs_data:
        faqs = FAQ.objects.all()
        faqs_data = [
            {
                'id': faq.id,
                'question': faq.get_question(lang),
                'answer': get_translated_answer(faq, lang),
            }
            for faq in faqs
        ]
        cache.set(cache_key, faqs_data, timeout=3600)

    return JsonResponse({'faqs': faqs_data}, safe=False, json_dumps_params={'ensure_ascii': False})


def faq_list(request):
    """
    Render the FAQ list page based on the selected language.
    
    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: A rendered HTML page displaying the FAQ list.
    """
    lang = request.GET.get('lang', 'en')
    faqs = FAQ.objects.all()
    
    faq_list = [
        {
            'question': faq.get_question(lang),
            'answer': get_translated_answer(faq, lang),
        }
        for faq in faqs
    ]

    return render(request, 'faq_list.html', {'faqs': faq_list, 'lang': lang})


def add_faq(request):
    """
    Handle the creation of a new FAQ.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: A redirect to the FAQ list after saving the new FAQ.
    """
    if request.method == 'POST':
        form = FAQForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('faq_list')
    else:
        form = FAQForm()

    return render(request, 'add_faq.html', {'form': form})


