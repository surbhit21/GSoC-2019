# Generated by Django 2.2.1 on 2019-05-26 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='model_file',
            field=models.FileField(upload_to='../files/model/'),
        ),
        migrations.AlterField(
            model_name='task',
            name='tsv_file',
            field=models.FileField(upload_to='../files/tsv/'),
        ),
    ]
