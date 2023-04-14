from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import datetime
from .models import Note


@login_required
def home(request):
    """
    Renders the home page of the logged in user with their notes.

    Parameters:
    -----------
    request: HttpRequest
        The HTTP request object sent by the user.

    Returns:
    --------
    render:
        Returns an HTTP response with the rendered HTML page containing the notes of the user.
    """
    
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
def delete_note(request, note_id):
    """
    Deletes a note belonging to the authenticated user.

    Parameters:
    request (HttpRequest): The request object used to generate this response.
    note_id (int): The id of the note to delete.

    Returns:
    HttpResponseRedirect: Redirects to the homepage of the app.

    Raises:
    Http404: If the note does not exist or if the user does not have permission to delete the note.
    """

    note = get_object_or_404(Note, pk=note_id, user=request.user)
    note.delete()
    messages.success(request, 'Note deleted successfully!')
    return redirect('minotes:home')

@login_required
def delete_all_notes(request):
    """
    Deletes all notes belonging to the authenticated user.

    Parameters:
    request (HttpRequest): The HTTP request object.

    Returns:
    HttpResponseRedirect: A redirect to the home page.

    """

    user_notes = Note.objects.filter(user=request.user)
    user_notes.delete()
    messages.success(request, 'All notes deleted successfully!')
    return redirect('minotes:home')
