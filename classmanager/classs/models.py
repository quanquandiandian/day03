from django.db import models

# Create your models here.
class TeamInfo(models.Model):
    name = models.CharField(max_length=10)
    def __str__(self):
        return self.name

class PeopleInfo(models.Model):
    name = models.CharField(max_length=10)


    classs = models.ForeignKey(TeamInfo,on_delete=models.CASCADE)