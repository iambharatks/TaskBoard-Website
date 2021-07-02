from django.db import models
from django.urls import reverse
# Create your models here.


class Task(models.Model):
    title = models.TextField(max_length=120,unique=True)
    date = models.DateField()
    time = models.TimeField()
    completed = models.BooleanField(default=False,blank=True)

    def get_absolute_url(self):
        return reverse('todo:todo-detail', kwargs={'id': self.id})
