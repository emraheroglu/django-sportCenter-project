# Generated by Django 3.0.8 on 2020-08-12 17:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_sss'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sss',
            name='ordernumber',
        ),
    ]