# Generated by Django 4.2.1 on 2023-05-27 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Token_Testing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('roll', models.CharField(max_length=243)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
    ]
