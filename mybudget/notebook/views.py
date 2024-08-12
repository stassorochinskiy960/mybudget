from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Note
from .forms import NoteForm


@login_required
def index_view(request):
    notes = Note.objects.filter(user=request.user)
    return render(request, 'budget/index.html', {'notes': notes})


@login_required
def add_note_view(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            return redirect('index')
    else:
        form = NoteForm()
    return render(request, 'notebook/add_note.html', {'form': form})


@login_required
def delete_note_view(request, pk):
    note = get_object_or_404(Note, pk=pk, user=request.user)
    if request.method == 'POST':
        note.delete()
        return redirect('index')
    return render(request, 'budget/index.html', {'note': note})
