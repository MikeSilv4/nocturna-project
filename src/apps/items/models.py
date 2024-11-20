from django.db import models

class Items(models.Model):

    name = models.CharField("Item name", max_length=256, null=False, default=None)
    brand = models.CharField("Item brand", max_length=128, null=True, default=None)
    model = models.CharField("Item model", max_length=128, null=True, default=None)
    description = models.CharField("Item description", max_length=512, null=False, default=None)
    value = models.DecimalField("Item value", max_digits=20, decimal_places=4, null=False, default=None)
    category = models.CharField("Item categoty", max_length=256, null=True, default=None)
    stock_quantity = models.IntegerField("Item stock quantity", default=0, null=False)
    image = models.CharField("Item Image", max_length=4096, null=True, default=None)
    
    class Meta:
        managed = True
        db_table = "items"
