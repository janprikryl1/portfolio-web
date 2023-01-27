# Generated by Django 4.0.4 on 2023-01-26 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Screenshot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=25)),
                ('image', models.ImageField(upload_to='screenshots/')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('w', 'web'), ('a', 'application'), ('g', 'game'), ('m', 'micro controller'), ('e', 'else')], default='w', max_length=1)),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('purpose', models.TextField()),
                ('repository', models.CharField(max_length=100)),
                ('date_time', models.DateTimeField(auto_now=True)),
                ('screenshots', models.ManyToManyField(to='main.screenshot')),
            ],
        ),
    ]
