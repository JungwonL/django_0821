from django.db import models

# Create your models here.

class CreatePost(models.Model):
    title = models.CharField('TITILE', max_length=100, blank=True)
    content = models.TextField('CONTENT')
    create_dt = models.DateTimeField('CREATE DATE', auto_now_add=True)
    modify_dt = models.DateTimeField('MODIFY DATE', auto_now_add=True)

    def __str__(self):
        return self.title