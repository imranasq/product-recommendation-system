# Generated by Django 4.1.1 on 2022-09-26 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(default='default.png', upload_to='images/profile/'),
        ),
    ]
