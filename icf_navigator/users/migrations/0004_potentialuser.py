# Generated by Django 3.1.2 on 2020-10-30 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20201004_2034'),
    ]

    operations = [
        migrations.CreateModel(
            name='PotentialUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=255, unique=True)),
            ],
        ),
    ]