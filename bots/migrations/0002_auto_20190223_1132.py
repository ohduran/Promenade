# Generated by Django 2.1.7 on 2019-02-23 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bots', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bot',
            name='username',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
