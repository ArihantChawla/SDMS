from django.db import models

# Create your models here.
class Student(models.Model):
	first_name =  models.CharField(max_length=100)
	middle_name =  models.CharField(max_length=100,null=True,blank=True)
	last_name =  models.CharField(max_length=100)
	address = models.CharField(max_length=100)
	city = models.CharField(max_length=30,default='Chandigarh')
	state = models.CharField(max_length=30,default='Chandigarh')
	branch =  models.CharField(max_length=10,default='CS')
	sid = models.IntegerField(default='17103036',primary_key=True)
	phone_no = models.CharField(max_length=10)
	dob = models.DateField()
	def __str__(self):
		return str(self.sid) + " : " + self.first_name + " " + self.last_name 
