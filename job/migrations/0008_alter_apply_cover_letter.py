# Generated by Django 4.1.4 on 2022-12-27 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0007_apply'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apply',
            name='cover_letter',
            field=models.TextField(max_length=100000),
        ),
    ]