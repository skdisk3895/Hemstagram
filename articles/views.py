from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ArticleForm, CommentForm
from .models import Article, Comment

@login_required
def article_list(request):
    articles = Article.objects.order_by('-created_at')
    context = {
        'articles': articles
    }
    return render(request, 'articles/article_list.html', context)

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

@login_required
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    form = CommentForm()
    print(request.path)
    context = {
        'article': article,
        'form': form
    }
    return render(request, 'articles/article_detail.html', context)

@login_required
def update_article(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:article_detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'form': form
    }
    return render(request, 'articles/form.html', context)

@login_required
@require_POST
def delete_article(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    article.delete()
    return redirect('articles:article_list')

@login_required
@require_POST
def create_comment(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.author = request.user
        comment.article = article
        comment.save()
    return redirect('articles:article_detail', article.pk)

@login_required
def update_comment(request, article_pk, comment_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.article = article
            comment.save()
            return redirect('articles:article_detail', article.pk)
    else:
        form = CommentForm(instance=comment)
    context = {
        'form': form,
        'article': article,
    }
    return render(request, 'articles/update_comment.html', context)

@login_required
def delete_comment(request, article_pk, comment_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.user == comment.author:
        comment.delete()
    return redirect('articles:article_detail', article.pk)

@login_required
def like_article(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    user = request.user
    # 만약 내가 이 글을 좋아요를 누른 상태라면
    if user in article.like_users.all():
        article.like_users.remove(user)
    # 내가 이 글을 좋아요를 누른 상태가 아니라면
    else:
        article.like_users.add(user)
    return redirect('articles:article_detail', article.pk)