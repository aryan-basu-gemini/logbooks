# Generated by Django 4.1.7 on 2023-05-21 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_contact_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='total',
            field=models.IntegerField(default=0),
        ),
    ]
