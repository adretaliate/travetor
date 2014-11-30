from django.db import models
from django.core.urlresolvers import reverse


class TrekCategory(models.Model):
	category_name=models.CharField(max_length=20)
	category_slug=models.SlugField(max_length=50)
	description=models.TextField()
	is_active=models.BooleanField(default=True)
	meta_keywords=models.CharField("Meta Keywords", max_length=255,help_text='coma-delimited set of SEO keywords for meta tag')
	meta_description=models.CharField("Meta description", max_length=255,help_text='content for Meta description tag')
	created_at=models.DateTimeField(auto_now_add=True)
	def get_absolute_url(self):
		return reverse('details.views',args=[str(self.category_slug)])
	def __unicode__(self):
		return self.category_name
	def __str__(self):
		return self.category_name
# Create your models here.

class Trek(models.Model):
	trek_name=models.CharField(max_length=70, unique=True)
	trek_categories=models.ForeignKey('TrekCategory',null=True)
	trek_rating=models.DecimalField(max_digits=3,decimal_places=2)
	trek_providerid=models.ForeignKey('Provider',null=True)
	trek_city=models.CharField(max_length=20)
	trek_state=models.CharField(max_length=20)
	trek_duration=models.PositiveSmallIntegerField()
	trek_difficulty=models.CharField(max_length=20)
	trek_Weather=models.CharField(max_length=50)
	trek_dateid=models.ManyToManyField('Trek_date',null=True)
	trek_price=models.FloatField()
	trek_overview=models.TextField()
	trek_itenary=models.TextField()
	trek_guidelines=models.TextField()
	trek_relatedtours=models.ManyToManyField('self',null=True,blank=True)
	#trek_relatedblogs=models.ManyToManyField('Blog')
	trek_slug=models.SlugField(max_length=70,unique=True,help_text='unique vlaue for trek details page URL, created from name')
	is_active=models.BooleanField(default=True)
	is_bestseller=models.BooleanField(default=False)
	is_featured=models.BooleanField(default=False)
	no_of_seats=models.PositiveSmallIntegerField()
	meta_keywords=models.CharField("Meta Keywords", max_length=255,help_text='coma-delimited set of SEO keywords for meta tag')
	meta_description=models.CharField("Meta description", max_length=255,help_text='content for Meta description tag')
	trek_created_at=models.DateTimeField(auto_now_add=True)
	trek_style=models.ManyToManyField('TrekStyle')
	def get_absolute_url(self):
		return reverse('travetor.details',args=[str(self.trek_slug)])
	def __unicode__(self):
		return self. trek_name
	def __str__(self):
		return self.trek_name

class Trek_date(models.Model):
	date=models.DateField()
	def __unicode__(self):
		return self.date

class Provider(models.Model):
	provider_name=models.CharField(max_length=50)
	def __unicode__(self):
		return self.provider_name
	def __str__(self):
		return self.provider_name

class TrekStyle(models.Model):
	CHOICES=(
		('Trekking','Trekking'),
		('Rafting','Rafting'),
		('Camping','Camping'),
		('Nigth Trek','Night trek'),
		)
	style=models.CharField(max_length=10,choices=CHOICES)
	def __unicode__(self):
		return self. style
	def __str__(self):
		return self.style

