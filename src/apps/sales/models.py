from django.db import models

# Create your models here.

class Sales(models.Model):

    name = models.CharField("Item name", max_length=256, null=False)
    brand = models.CharField("Item brand", max_length=128, null=True, default=None)
    model = models.CharField("Item model", max_length=128, null=True, default=None)
    description = models.CharField("Item description", max_length=512, null=False, default=None)
    value = models.DecimalField("Item value", max_digits=20, decimal_places=4, null=False, default=None)
    quantity = models.BigIntegerField("Quantity field", null=False)
    #foregnkey
    user = models.BigIntegerField("User ID field", null=False)

    class Meta:
        managed = True
        db_table = "sales"