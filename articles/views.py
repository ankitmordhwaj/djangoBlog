from django.shortcuts import render
from .models import Article

# Create your views here.
def artice_list(request):
    articles = Article.objects.all().order_by('date')

    return render(request, 'articles/articles_list.html', {'articles': articles})