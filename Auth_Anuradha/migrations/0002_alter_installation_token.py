# Generated by Django 4.0.6 on 2022-07-14 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auth_Anuradha', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='installation',
            name='token',
            field=models.CharField(max_length=1000),
        ),
    ]
