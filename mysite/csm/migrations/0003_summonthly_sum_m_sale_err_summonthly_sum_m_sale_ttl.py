# Generated by Django 4.1.3 on 2022-12-06 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csm', '0002_alter_datamonthly_str_code_alter_summonthly_str_code_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='summonthly',
            name='sum_m_sale_err',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='summonthly',
            name='sum_m_sale_ttl',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
