from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField

class Category(models.Model):
	name = models.CharField(max_length = 255)

	def __str__(self):
		return self.name 

	def get_absolute_url(self):
		#return reverse('article-detail', args=(str(self.id)))
		return reverse('home')

class Post(models.Model):
	title = models.CharField(max_length = 255)
	title_tag = models.CharField(max_length = 255)
	author = models.ForeignKey(User, on_delete = models.CASCADE)
	#snippet = models.CharField(max_length = 255, default = 'Click Link Above To Read Blog Post...')
	category = models.CharField(max_length = 255, default = 'None')
	body = RichTextField(blank=True, null=True)
	# body = models.TextField()
	post_date = models.DateField(auto_now_add=True)
	Likes = models.ManyToManyField(User, related_name='blog_posts')
	# unlikes = models.ManyToManyField(User, related_name='blog_posts')
	

	def __str__(self):
		return self.title + ' | ' + str(self.author)

	def get_absolute_url(self):
		#return reverse('article-detail', args=(str(self.id)))
		return reverse('home')


# class Comment(models.Model):
# 	 post = models.ForeingKey(Post, related_name="comments", on_delete = models.CASCADE)
# 	 name = models.CharField(max_lenght=255)
# 	 body = models.TextField()
# 	 date_added = model.DateTimeField(auto_now_add=True)

# 	 def __str__(self):
# 	 	return '%s - %s' % (self.post.title(), self.name)
			