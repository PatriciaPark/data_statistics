# Generated by Django 4.1.3 on 2022-11-22 05:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('csd', '0004_rename_prd_code_invoicedaily_inv_prd_code_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='invoicedaily',
            old_name='inv_prd_code',
            new_name='prd_code',
        ),
        migrations.RenameField(
            model_name='invoicedaily',
            old_name='inv_str_code',
            new_name='str_code',
        ),
    ]
