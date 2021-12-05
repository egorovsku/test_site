from django.db import models

class Task(models.Model):
    title = models.CharField('Назание', max_length=50)
    task = models.TextField('Описание',)

    def __str__(self):
        return self.title

