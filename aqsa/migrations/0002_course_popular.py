# Generated by Django 3.2.4 on 2021-06-19 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aqsa', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='popular',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
