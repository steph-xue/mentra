# Generated by Django 5.0.4 on 2025-03-08 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_description',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='category',
            name='icon_url',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='category',
            name='category_name',
            field=models.CharField(default='', max_length=30),
        ),
    ]
