# Generated by Django 4.1.3 on 2022-12-20 02:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('csd', '0016_remove_invoicedaily_prd_code_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoicedaily',
            name='prd_code',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='csd.product'),
        ),
        migrations.AddField(
            model_name='invoicedaily',
            name='str_code',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='csd.store'),
        ),
    ]
