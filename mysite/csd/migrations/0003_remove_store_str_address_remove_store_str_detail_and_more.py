# Generated by Django 4.1.3 on 2022-11-18 09:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('csd', '0002_datadaily_invoicedaily_product_store_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='store',
            name='str_address',
        ),
        migrations.RemoveField(
            model_name='store',
            name='str_detail',
        ),
        migrations.RemoveField(
            model_name='store',
            name='str_use',
        ),
    ]
