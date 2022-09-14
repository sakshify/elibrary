from django.db import models
from django.db import connections


# Create your models here.
class books(models.Model):
    Book_id=models.IntegerField(primary_key=True)
    Book_name=models.CharField(max_length=80)
    Aisle_number=models.IntegerField()
    class Meta:
        db_table="books"
