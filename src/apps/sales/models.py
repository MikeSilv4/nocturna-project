from django.db import models

class Sale(models.Model):
    user = models.BigIntegerField(null=False)
    itemname = models.CharField(max_length=256, null=False, default="")
    itemdescription = models.CharField(max_length=512, null=False, default="")
    itemvalue = models.DecimalField(max_digits=20, decimal_places=4, null=False, default=0.0)
    salequantity = models.IntegerField(null=False, default=0)
    salevalue = models.DecimalField(max_digits=20, decimal_places=4, null=False, default=0.0)
    saledate = models.DateField(null=False, auto_now_add=True)

    def __str__(self):
        return 
