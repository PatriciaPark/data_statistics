# Generated by Django 4.1.3 on 2022-12-20 02:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('csd', '0015_invoicedaily_prd_code_invoicedaily_str_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoicedaily',
            name='prd_code',
        ),
        migrations.RemoveField(
            model_name='invoicedaily',
            name='str_code',
        ),
    ]
