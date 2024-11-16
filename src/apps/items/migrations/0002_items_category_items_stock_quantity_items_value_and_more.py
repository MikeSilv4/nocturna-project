# Generated by Django 4.2.16 on 2024-10-10 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='category',
            field=models.CharField(default=None, max_length=256, null=True, verbose_name='Item categoty'),
        ),
        migrations.AddField(
            model_name='items',
            name='stock_quantity',
            field=models.IntegerField(default=0, verbose_name='Item stock quantity'),
        ),
        migrations.AddField(
            model_name='items',
            name='value',
            field=models.DecimalField(decimal_places=4, default=None, max_digits=20, verbose_name='Item value'),
        ),
        migrations.AlterField(
            model_name='items',
            name='brand',
            field=models.CharField(default=None, max_length=128, null=True, verbose_name='Item brand'),
        ),
        migrations.AlterField(
            model_name='items',
            name='description',
            field=models.CharField(default=None, max_length=512, verbose_name='Item description'),
        ),
        migrations.AlterField(
            model_name='items',
            name='model',
            field=models.CharField(default=None, max_length=128, null=True, verbose_name='Item model'),
        ),
        migrations.AlterField(
            model_name='items',
            name='name',
            field=models.CharField(default=None, max_length=256, verbose_name='Item name'),
        ),
    ]