# Generated by Django 4.0.4 on 2023-01-26 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=20)),
                ('message', models.TextField()),
                ('date_time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
