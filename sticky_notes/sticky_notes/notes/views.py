from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.urls import reverse_lazy
from .models import Note
# Create your views here.


class NoteListView(ListView):
    """
    This view handles the listing of all notes.
    """
    model = Note
    template_name = 'notes/note_list.html'
    context_object_name = 'notes'


class NoteDetailView(DetailView):
    """
    This view handles the details of a note.
    """
    model = Note
    template_name = 'notes/note_detail.html'


class NoteCreateView(CreateView):
    """
    This view handles the creation of a new note.
    """
    model = Note
    fields = ['title', 'content']
    template_name = 'notes/note_form.html'
    success_url = reverse_lazy('note-list')


class NoteUpdateView(UpdateView):
    """
    This view handles the update of a note.
    """
    model = Note
    fields = ['title', 'content']
    template_name = 'notes/note_form.html'
    success_url = reverse_lazy('note-list')


class NoteDeleteView(DeleteView):
    """
    This view handles the deletion of a note.
    """
    model = Note
    template_name = 'notes/note_confirm_delete.html'
    success_url = reverse_lazy('note-list')
