from django.db import models

# Create your models here.
class Study(models.Model):
    name = models.CharField(max_length=255)
    year = models.SmallIntegerField()
    def __unicode__(self):
        return self.name
class Member(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    nr = models.IntegerField()
    postal_code = models.IntegerField()
    city = models.CharField(max_length=255)
    study = models.ForeignKey(Study)
    #year = models.ForeignKey(Study)
    def __unicode__(self):
        return "%s, %s" %(self.last_name, self.first_name)
