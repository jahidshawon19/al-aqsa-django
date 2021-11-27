# Generated by Django 3.2.4 on 2021-06-23 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aqsa', '0009_slider_sponsor_testimonial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=40)),
                ('subject', models.CharField(blank=True, max_length=1000)),
                ('phone', models.CharField(blank=True, max_length=15)),
                ('message', models.TextField()),
                ('status', models.CharField(choices=[('New', 'New'), ('Read', 'Read'), ('Closed', 'Closed')], default='New', max_length=40)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
