from django.db import models

class Items(models.Model):

    name = models.CharField("Item name", max_length=256, null=False)
    brand = models.CharField("Item brand", max_length=128, null=True)
    model = models.CharField("Item model", max_length=128, null=True)
    description = models.CharField("Item description", max_length=512, null=True)

    class Meta:
        managed = True
        db_table = "items"