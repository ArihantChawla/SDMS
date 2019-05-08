from django.db import models

# Create your models here.
class librarylog(models.Model):
    book_name =  models.CharField(max_length=400)
    book_id = models.IntegerField(default='42081710',primary_key=True)
    author_first_name =  models.CharField(max_length=100)
    author_middle_name =  models.CharField(max_length=100,null=True,blank=True)
    author_last_name =  models.CharField(max_length=100)
    year_of_publication = models.CharField(max_length=4,default='2019')
    sid =  models.ForeignKey('Student.Student',on_delete=models.CASCADE)
    def __str__(self):
        return str(self.sid) + " : " + str(self.book_id) + " : " + str(self.book_name)
