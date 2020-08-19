# Generated by Django 3.0.7 on 2020-08-19 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=125)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField(max_length=255)),
                ('city', models.CharField(max_length=150)),
                ('zipcode', models.CharField(max_length=15)),
            ],
        ),
    ]
