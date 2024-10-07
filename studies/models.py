# studies/models.py
from django.db import models

class Study(models.Model):
    title = models.CharField(max_length=200)  # Title of the study
    description = models.TextField()  # Description of the study
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set when a study is created

    def __str__(self):
        return self.title  # Return the title as the string representation of the study
