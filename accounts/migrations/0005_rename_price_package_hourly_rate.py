# Generated by Django 3.2.5 on 2021-07-19 04:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20210719_0348'),
    ]

    operations = [
        migrations.RenameField(
            model_name='package',
            old_name='price',
            new_name='hourly_rate',
        ),
    ]