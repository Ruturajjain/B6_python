from django.db import models

# Create your models here.
print("in models.py")

class InActivebooks(models.Manager):
    def get_queryset(self):
        return super(InActivebooks,self).get_queryset().filter(is_active = 0)


class Book(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    qty = models.IntegerField()
    is_active = models.BooleanField(default=1)
    Inactive_objects = InActivebooks()
    objects = models.Manager()
    
    class Meta:
        db_table = "book"
        
    def __str__(self):
        return self.name
    
#builtin apps--auth,session,admin.contenttypes
#user defindes apps-- book


class Employee(models.Model):  
    first_name = models.CharField(max_length=30)  
    last_name = models.CharField(max_length=30)  
    mobile = models.CharField(max_length=10)  
    email = models.EmailField()  
    
    
    class Meta:
        db_table = "emp"
        
    def __str__(self):
        return self.first_name
    
    
