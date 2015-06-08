from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
	user = models.ForeignKey(User)
	post_text = models.CharField(max_length=512)
	pub_date = models.DateTimeField('date published')
	likes = models.IntegerField(default=0)