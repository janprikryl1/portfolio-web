# Generated by Django 3.2.7 on 2023-01-29 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_screenshot_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='icon',
            field=models.ImageField(default=None, upload_to='project_icons/'),
        ),
    ]
