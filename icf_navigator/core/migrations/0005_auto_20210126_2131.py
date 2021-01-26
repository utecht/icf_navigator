# Generated by Django 3.1.2 on 2021-01-26 21:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20201206_1750'),
    ]

    operations = [
        migrations.CreateModel(
            name='CannedText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=50, unique=True)),
                ('text', models.TextField(blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='canned_logic',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='question',
            name='canned',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.cannedtext'),
        ),
    ]
