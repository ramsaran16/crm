from django.db import models
import datetime

# Create your models here.
# def year_choice():
#     return [(r,r) for r in range(2010, datetime.date.today().year+1)]
# def current_year():
#     return datetime.date.today().year

class add_form(models.Model):
    name            = models.CharField(max_length = 120)
    email        = models.EmailField()
    phone    = models.CharField(max_length=12)
    yop             = models.IntegerField()
    degree          = models.CharField(max_length = 120)
    status          = models.CharField(max_length = 120)
    def __str__(self):
        return ("%s" %(self.name))
    
class Item(models.Model):
    name = models.TextField(max_length=191)
    empid = models.CharField(max_length = 20, primary_key = True, unique = True)
    doj = models.DateField(auto_now = False, auto_now_add = False)
    dor = models.DateField(auto_now = False, auto_now_add = False)
    lws = models.CharField(max_length=20)

    def __str__(self):
        return ("%s" %(self.name))