# Generated by Django 3.2.5 on 2021-07-19 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_order_package'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Active', 'Active'), ('On Hold', 'On Hold'), ('Inactive', 'Inactive')], max_length=200, null=True),
        ),
    ]
