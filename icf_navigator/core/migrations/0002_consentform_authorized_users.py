# Generated by Django 3.1.2 on 2020-10-30 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_potentialuser'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='consentform',
            name='authorized_users',
            field=models.ManyToManyField(to='users.PotentialUser'),
        ),
    ]