from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature


def index(request):
    feature1 = Feature()
    feature1.id = 0
    feature1.name = 'Fast'
    feature1.details = 'Our service is very quick'

    feature2 = Feature()
    feature2.id = 1
    feature2.name = 'Reliable'
    feature2.details = 'Our service is very reliable'

    feature3 = Feature()
    feature3.id = 2
    feature3.name = 'Easy to Use'
    feature3.details = 'Our service is very easy to use'

    feature4 = Feature()
    feature4.id = 3
    feature4.name = 'Affordable'
    feature4.details = 'Our service is very affordable'

    features = [feature1, feature2, feature3, feature4]

    return render(request, 'index.html', {'features': features})

def counter(request):
    text = request.POST['text']
    word_count = len(text.split())
    return render(request, 'counter.html', {'word_count': word_count})

