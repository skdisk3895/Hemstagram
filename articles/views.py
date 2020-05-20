from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from .models import Article
from .forms import ArticleForm

@require_GET
@login_required
def article_list(request):
    articles = Article.objects.order_by('-created_at')
    context = {
        'articles': articles
    }
    return render(request, 'articles/article_list.html', context)

@require_http_methods(['GET', 'POST'])
@login_required
def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('articles:article_detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form
    }
    return render(request, 'articles/form.html', context)

@require_GET
@login_required
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    context = {
        'article': article
    }
    return render(request, 'articles/article_detail.html', context)