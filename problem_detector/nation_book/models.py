from django.db import models

# Create your models here.
class ProblemStatements(models.Model):
    statement_id=models.IntegerField()
    statement_name=models.CharField(max_length=200)
    statement_img=models.ImageField()
    statement_desc=models.CharField(max_length=500)

    
