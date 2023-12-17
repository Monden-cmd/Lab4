from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Task(models.Model):
    category = models.ForeignKey('tasks.Category', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    deadline = models.DateTimeField()
    priority = models.IntegerField()
    status = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
