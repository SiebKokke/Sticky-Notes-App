from django.db import models

# Create your models here.


class Note(models.Model):
    """
    This is the model for the sticky notes.
    It contains a title and content for each note.
    """
    title = models.CharField(max_length=150)
    content = models.TextField()

    def __str__(self):
        return self.title
