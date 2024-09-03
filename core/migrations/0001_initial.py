# Generated by Django 5.1 on 2024-09-03 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=25)),
                ('subject', models.CharField(max_length=250)),
                ('message', models.TextField()),
            ],
        ),
    ]
