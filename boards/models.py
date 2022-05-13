from django.db import models
from django.contrib.auth.models import User
import uuid
import os


# Create your models here.
class Board(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_last_post(self):
        try:
            return Topic.objects.filter().order_by("last_update").first().last_update
        except AttributeError:
            pass


def user_directory_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid.uuid4().hex[:10], ext)
    return os.path.join("files", filename)


class Topic(models.Model):
    subject = models.CharField(max_length=255, null=True)
    message = models.TextField(max_length=4000, null=True)
    file = models.FileField(upload_to=user_directory_path, null=True)
    file_path = models.TextField(null=True)
    last_update = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey(Board, callable, related_name='topics')
    starter = models.ForeignKey(User, callable, related_name='topics')

    def __str__(self):
        return self.subject
