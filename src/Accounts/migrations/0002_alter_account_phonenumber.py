# Generated by Django 4.0 on 2021-12-13 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='PhoneNumber',
            field=models.CharField(max_length=11),
        ),
    ]
