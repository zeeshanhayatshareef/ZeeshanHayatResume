# Generated by Django 4.0.3 on 2022-03-29 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0007_alter_about_myself'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='degree_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='education',
            name='degree_title',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='experience',
            name='institution',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='experience',
            name='work_as',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='skill',
            name='s_name',
            field=models.CharField(max_length=50),
        ),
    ]
