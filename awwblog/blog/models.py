from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Post Model
class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
        )
