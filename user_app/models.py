from django.db import models
from django.contrib.auth.models import User
# Create your models here.

User.add_to_class('photo', models.ImageField(upload_to='avatars', blank=True, null=True))
User._meta.get_field('email')._unique = True
