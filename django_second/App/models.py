from django.db import models

# Create your models here.
class Person(models.Model):
    p_name = models.CharField(max_length=16, unique=True)
    p_age = models.IntegerField(default=1, db_column='age')
    # flase = man
    p_sex = models.BooleanField(default=False, db_column='sex')

    class Meta:
        db_table = 'People'