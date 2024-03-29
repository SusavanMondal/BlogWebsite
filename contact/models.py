from django.db import models

# Create your models here.


# Create your models here.
class contact_list(models.Model):
    Email=models.CharField(max_length=100, blank=False)
    Address=models.TextField(max_length=800, blank=False)
    # description1=models.TextField(max_length=100, blank=False)
    phone=models.CharField(max_length=100, blank=False)
    

    def __str__(self):
        return self.Email
    

class contactform(models.Model):
    Name=models.CharField(max_length=100, blank=False)
    Email=models.CharField(max_length=100, blank=False)
    Subject=models.CharField(max_length=400, blank=False)
    Message=models.CharField(max_length=800, blank=False)

    def __str__(self):
        return self.Name
