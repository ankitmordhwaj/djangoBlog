from django.shortcuts import render
from .models import Article
# from django.http import HttpResponse

# Create your views here.
def artice_list(request):
    articles = Article.objects.all().order_by('date')

    return render(request, 'articles/articles_list.html', {'articles': articles})


def artice_detail(request, slug):
    # articles = Article.objects.all().order_by('date')
    article = Article.objects.get(slug = slug)

    return render(request, 'articles/article_detail.html', {'article': article})

    # return HttpResponse(slug)
