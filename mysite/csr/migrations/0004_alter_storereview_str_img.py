# Generated by Django 4.1.5 on 2023-02-01 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csr', '0003_alter_storereview_str_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storereview',
            name='str_img',
            field=models.ImageField(upload_to='../media/%Y%m%d/'),
        ),
    ]
