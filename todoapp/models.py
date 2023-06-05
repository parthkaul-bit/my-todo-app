from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
    
class ToDoItem(models.Model):
    STATUS_CHOICES = [
        ('OPEN', 'Open'),
        ('WORKING', 'Working'),
        ('DONE', 'Done'),
        ('OVERDUE', 'Overdue'),
    ]

    timestamp = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100,editable=True)
    description = models.TextField(max_length=1000,blank=True)
    due_date = models.DateField(blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='OPEN')

    def __str__(self):
        return self.title
