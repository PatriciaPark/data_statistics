# Generated by Django 4.1.5 on 2023-01-31 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csr', '0002_alter_storereview_str_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storereview',
            name='str_img',
            field=models.ImageField(upload_to='./media/%Y%m%d/'),
        ),
    ]
