# Generated by Django 4.2.1 on 2023-05-16 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='data',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
