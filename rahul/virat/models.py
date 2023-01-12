from django.db import models
from django.contrib.auth.models import User
from django.db import migrations

# Create your models here.
# class Day(models.Model):
# 	name = models.CharField(max_length=50,unique=True)

# 	def __str__(self):
# 		return self.name
# class Night(models.Model):
# 	number = models.ForeignKey(Day,on_delete=models.CASCADE)
# 	date = models.DateField()

# 	def __str__(self):
# 		return str(self.date)
# class MidDay(models.Model):
# 	row = models.ForeignKey(Night,on_delete=models.CASCADE)
# 	url = models.URLField(unique=True)

# 	def __str__(self):
# 		return self.row
# class User(models.Model):
# 	top_name = models.CharField(max_length=25,unique=True)

# 	def __str__(self):
# 		return self.top_name

class UserProfileInfo(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	portfolio_site = models.URLField(blank=True)
	profile_pic = models.ImageField(upload_to = 'profile_pics',blank=True)

	def __str__(self):
		return self.user.username