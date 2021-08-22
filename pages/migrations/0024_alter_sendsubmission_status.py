# Generated by Django 3.2.1 on 2021-05-21 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0023_sendsubmission_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sendsubmission',
            name='status',
            field=models.CharField(choices=[('In Process', 'In process'), ('Accepted', 'Accepted'), ('Failed', 'Failed')], default='In Process', max_length=10),
        ),
    ]
