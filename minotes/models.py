from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Note(models.Model):
    """
    A model representing a note created by a user.

    Attributes:
    -----------
    user : ForeignKey
        A foreign key to the User model representing the user who created the note.
    title : CharField
        A char field representing the title of the note.
    content : TextField
        A text field representing the content of the note.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        """
        Return a string representation of the note's title.

        Returns:
        --------
        str
            A string representation of the note's title.
        """
        return self.title