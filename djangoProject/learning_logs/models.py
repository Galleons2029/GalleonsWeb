from django.db import models

"""
A model tells Django how to work with the data that will be stored in the app.
A model is a class, it has attributes and methods。
"""
# Create your models here.

class Topic(models.Model):
    """A topic the user is learning about."""
    """Inherits from Model - a parent class included in Django 
    that defines a model's basic functionality."""
    text = models.CharField(max_length=200)
    # use CharField when want to stor a small amount of text.
    data_added = models.DateTimeField(auto_now_add=True)
    # We pass the argument auto_now_add=True, which tells Django to
    # automatically set this attribute to the current date and time
    # whenever the user creates a new topic.

    def __str__(self):
        """Return a string representation of the model."""
        return self.text
        # Here we’ve written a __str__() method that returns
        # the value assigned to the text attribute.


class Entry(models.Model):
    """Something specific learned about a topic."""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    # ForeignKey is a reference to another record in the database.
    # This is the code that connects each entry to a specific topic.
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Return a simple string representing the entry."""
        return f"{self.text[:50]}..."

