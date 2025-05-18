from django.test import TestCase
from django.urls import reverse
from .models import Note
# Create your tests here.


class NoteTests(TestCase):
    def setUp(self):
        self.note = Note.objects.create(
            title="Test Note",
            content="This is a test."
        )
    """
    Test case for the Note model and views.
    First one tests note creatiom.
    """
    def test_note_creation(self):
        self.assertEqual(self.note.title, "Test Note")
        self.assertEqual(str(self.note), "Test Note")
    """
    Tests the note list view.
    """
    def test_note_list_view(self):
        response = self.client.get(reverse('note-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Note")
    """
    Tests the note detail view.
    """
    def test_note_detail_view(self):
        response = self.client.get(reverse('note-detail', args=[self.note.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.note.title)
    """
    Tests the note create view.
    """
    def test_note_create_view(self):
        response = self.client.post(reverse('note-create'), {
            'title': 'New Note',
            'content': 'Created through test'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Note.objects.count(), 2)
    """
    Tests the note update view.
    """
    def test_note_update_view(self):
        response = self.client.post(
            reverse('note-update', args=[self.note.id]),
            {
                'title': 'Updated Title',
                'content': 'Updated content'
            }
        )
        self.assertEqual(response.status_code, 302)
        self.note.refresh_from_db()
        self.assertEqual(self.note.title, 'Updated Title')
    """
    Tests the note delete view.
    """
    def test_note_delete_view(self):
        response = self.client.post(
            reverse('note-delete', args=[self.note.id])
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Note.objects.count(), 0)
