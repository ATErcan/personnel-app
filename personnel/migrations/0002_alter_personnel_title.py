# Generated by Django 4.2.2 on 2023-06-12 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personnel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personnel',
            name='title',
            field=models.SmallIntegerField(choices=[(1, 'Junior'), (2, 'Mid'), (3, 'Senior'), (4, 'Team Lead')]),
        ),
    ]
