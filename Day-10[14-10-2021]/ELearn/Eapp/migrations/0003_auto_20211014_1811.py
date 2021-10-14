# Generated by Django 3.0 on 2021-10-14 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Eapp', '0002_auto_20211014_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('F', 'Female'), ('M', 'Male')], max_length=10),
        ),
        migrations.AlterField(
            model_name='user',
            name='usrole',
            field=models.IntegerField(choices=[(2, 'Instructor'), (1, 'Student')], default=1, max_length=20),
        ),
    ]