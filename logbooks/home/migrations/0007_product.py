# Generated by Django 4.1.7 on 2023-06-21 11:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_contact_primary'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('description', models.TextField()),
                ('name', models.CharField(max_length=200)),
                ('primary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.contact')),
            ],
        ),
    ]