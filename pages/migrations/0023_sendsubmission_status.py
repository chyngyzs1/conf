# Generated by Django 3.2.1 on 2021-05-21 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0022_sendsubmission_send_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='sendsubmission',
            name='status',
            field=models.CharField(blank=True, choices=[('In Process', 'In process'), ('Accepted', 'Accepted'), ('Failed', 'Failed')], max_length=10, null=True),
        ),
    ]
