# Generated by Django 3.2.5 on 2021-07-17 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ragus', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='door',
            name='acme_device_id',
            field=models.CharField(default=0, max_length=8),
            preserve_default=False,
        ),
    ]