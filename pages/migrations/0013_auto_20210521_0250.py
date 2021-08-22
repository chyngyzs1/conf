# Generated by Django 3.2.1 on 2021-05-20 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0012_remove_sendsubmission_upload_abstract'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sendsubmission',
            name='talk_s',
        ),
        migrations.AddField(
            model_name='sendsubmission',
            name='upload_abstract',
            field=models.FileField(blank=True, null=True, upload_to='uploads/', verbose_name='upload_abstract'),
        ),
    ]