# Generated by Django 3.0.2 on 2020-01-26 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0005_auto_20200126_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='birth',
            field=models.DateField(default='1970-01-01'),
        ),
    ]
