from django.db import models

# Create your models here.
class Game(models.Model):
	name		=		models.CharField(max_length = 50)
	description =		models.TextField(max_length = 1000)
	year		=		models.CharField(max_length = 4)
	slug		=		models.SlugField(blank=True)	
