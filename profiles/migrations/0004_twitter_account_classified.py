# Generated by Django 2.1 on 2018-08-31 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_twitter_account_screen_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='twitter_account',
            name='classified',
            field=models.BooleanField(default=False),
        ),
    ]