from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from django.http import JsonResponse
from .models import Photo, Comment
from .forms import PhotoForm, CommentForm

@login_required
@require_GET
def photo_list(request):
    photos = Photo.objects.order_by('-created_at')
    form = CommentForm()
    context = {
        'photos': photos,
        'form': form
    }
    return render(request, 'photos/photo_list.html', context)

@login_required
@require_http_methods(['GET', 'POST'])
def create_photo(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.author = request.user
            photo.save()
            return redirect('photos:photo_list')
    else:
        form = PhotoForm()
    context = {
        'form': form
    }
    return render(request, 'photos/form.html', context)

@require_GET
@login_required
def photo_detail(request, photo_pk):
    photo = get_object_or_404(Photo, pk=photo_pk)
    form = CommentForm()
    context = {
        'photo': photo,
        'form': form
    }
    return render(request, 'photos/photo_detail.html', context)

@login_required
def update_photo(request, photo_pk):
    photo = get_object_or_404(Photo, pk=photo_pk)
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES, instance=photo)
        if form.is_valid():
            print('OK')
            form.save()
            return redirect('photos:photo_detail', photo.pk)
    else:
        form = PhotoForm(instance=photo)
    context = {
        'form': form
    }
    return render(request, 'photos/form.html', context)

@login_required
def delete_photo(request, photo_pk):
    photo = get_object_or_404(Photo, pk=photo_pk)
    if request.user == photo.author:
        photo.delete()
    else:
        messages.error(request, '권한이 없습니다.')
    return redirect('photos:photo_list')

@login_required
@require_POST
def create_comment(request, photo_pk):
    photo = get_object_or_404(Photo, pk=photo_pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.author = request.user
        comment.photo = photo
        comment.save()
    return redirect('photos:photo_detail', photo.pk)

@login_required
def update_comment(request, photo_pk, comment_pk):
    photo = get_object_or_404(Photo, pk=photo_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment.save()
            return redirect('photos:photo_detail', photo.pk)
    else:
        form = CommentForm(instance=comment)
    context = {
        'form': form,
        'photo': photo,
    }
    return render(request, 'articles/update_comment.html', context)

@login_required
def delete_comment(request, photo_pk, comment_pk):
    photo = get_object_or_404(Photo, pk=photo_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.user == comment.author:
        comment.delete()
    return redirect('photos:photo_detail', photo.pk)

@login_required
def like_photo(request, photo_pk):
    photo = get_object_or_404(Photo, pk=photo_pk)
    user = request.user
    # 만약 내가 이 글을 좋아요를 누른 상태라면
    if user in photo.like_users.all():
        photo.like_users.remove(user)
        is_liked = False
    # 내가 이 글을 좋아요를 누른 상태가 아니라면
    else:
        photo.like_users.add(user)
        is_liked = True
    data = {
        'is_liked': is_liked,
        'like_count': photo.like_users.count()
    }
    return JsonResponse(data)

def like_comment(request, photo_pk, comment_pk):
    photo = get_object_or_404(Photo, pk=photo_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)
    user = request.user
    if user in comment.like_users.all():
        comment.like_users.remove(user)
        is_liked = False
    else:
        comment.like_users.add(user)
        is_liked = True
    data = {
        'is_liked': is_liked,
        'like_count': comment.like_users.count()
    }
    return JsonResponse(data)