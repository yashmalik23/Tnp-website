from django.db import models
import datetime
from django.core.urlresolvers import reverse
# Create your models here.

# Profiles
class profiles(models.Model):
	branch = models.CharField(max_length=250)
	name = models.CharField(max_length=250)
	regn_no =models.CharField(max_length=250)
	CGPA =models.CharField(max_length=20)
	email = models.CharField(max_length=250)
	skill1 = models.CharField(max_length=250)
	skill2 = models.CharField(max_length=250)
	skill3 = models.CharField(max_length=250)
	pic=models.FileField()

	def __str__(self):
		return self.branch+'-'+self.name+'-'+self.regn_no+'-'+self.CGPA+'-'+self.email+'-'+self.skill1+'-'+self.skill2+'-'+self.skill3

#Downloads
class download(models.Model):
	name = models.CharField(max_length=250)
	file = models.FileField()

	def __str__(self):
		return self.name

#Alumni
class alumni(models.Model):
	pic = models.FileField()
	name = models.CharField(max_length=250)
	rank = models.CharField(max_length=250)
	company = models.CharField(max_length=250)
	byte = models.CharField(max_length=2500)
	assign =models.IntegerField()

	def __str__(self):
		return self.name +'-'+self.rank+'-'+self.company +'-'+self.byte

#Recruiters
class recruiters(models.Model):
	logo = models.FileField()
	name = models.CharField(max_length=250)

	def __str__(self):
		return self.name

#tnpteam
class team(models.Model):
	rank = models.CharField(max_length=250)
	name = models.CharField(max_length=250)
	designation = models.CharField(max_length=250)
	email = models.CharField(max_length=250)
	phone = models.CharField(max_length=20)

	def __str__(self):
		return self.rank +'-'+self.name+'-'+self.designation +'-'+self.email+'-'+self.phone

#Placed Students
class placement(models.Model):
	pic = models.FileField()
	name = models.CharField(max_length=250)
	company = models.CharField(max_length=250)

	def __str__(self):
		return self.name+'-'+self.company

class gallery(models.Model):
	name=models.CharField(max_length=500)
	pic=models.FileField()

	def __str__(self):
		return self.name