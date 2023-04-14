from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import datetime
from .models import Note


@login_required
def home(request):
    now = datetime.now() # get the current datetime
    username = request.user.username
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        new_note = Note(title=title, content=content, user=request.user)
        new_note.save()
        messages.success(request, 'Note added successfully!')
        return redirect('minotes:home')
    notes = Note.objects.filter(user=request.user)
    return render(request, 'index.html', {'notes': notes, 'now': now, 'username': username})

@login_required 
def update_note(request, note_id):
    note = get_object_or_404(Note, pk=note_id)

    if request.user != note.user:
        return HttpResponseForbidden()

    if request.method == 'POST':
        note.title = request.POST['title']
        note.content = request.POST['content']
        note.save()
        return redirect('minotes:home')

    context = {'note': note}
    return render(request, 'update_note.html', context)

@login_required
def delete_note(request, note_id):
    note = get_object_or_404(Note, pk=note_id, user=request.user)
    note.delete()
    messages.success(request, 'Note deleted successfully!')
    return redirect('minotes:home')

@login_required
def delete_all_notes(request):
    user_notes = Note.objects.filter(user=request.user)
    user_notes.delete()
    messages.success(request, 'All notes deleted successfully!')
    return redirect('minotes:home')
