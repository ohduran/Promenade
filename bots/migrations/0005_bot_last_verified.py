# Generated by Django 2.1.7 on 2019-02-23 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bots', '0004_auto_20190223_1739'),
    ]

    operations = [
        migrations.AddField(
            model_name='bot',
            name='last_verified',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
