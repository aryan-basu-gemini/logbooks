# Generated by Django 4.1.7 on 2023-06-21 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='primary',
            field=models.CharField(default=0, max_length=100),
        ),
    ]
