from django.db import models
from django.core.urlresolvers import reverse


# Create your models here.

class Tag(models.Model):
	slug = models.SlugField(max_length=200, unique = True)
	
	def __str__(self):
		return self.slug

	def get_absolute_url(self):
		return reverse("tag_index", kwargs = {"slug" : self.slug})


class Article(models.Model):
	title = models.CharField(max_length = 100) #title of blog
	category = models.CharField(max_length=200, blank = True) #blog tag
#	category = models.ManyToManyField(Tag)
	date_time = models.DateTimeField(auto_now_add = True) #blog date time
	content = models.TextField(blank = True, null = True) #blog content

	def __str__(self):
		return self.title
	
	class Meta:
		ordering = ['-date_time']


