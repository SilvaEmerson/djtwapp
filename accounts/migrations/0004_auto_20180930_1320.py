# Generated by Django 2.1 on 2018-09-30 16:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20180825_1312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='vote_account',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='profiles.Twitter_account'),
        ),
    ]