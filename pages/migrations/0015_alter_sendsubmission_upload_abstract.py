# Generated by Django 3.2.1 on 2021-05-20 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0014_alter_sendsubmission_upload_abstract'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sendsubmission',
            name='upload_abstract',
            field=models.FileField(upload_to='testing/', verbose_name='upload_abstract'),
        ),
    ]