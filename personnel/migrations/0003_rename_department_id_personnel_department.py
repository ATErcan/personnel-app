# Generated by Django 4.2.2 on 2023-06-13 09:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personnel', '0002_alter_personnel_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='personnel',
            old_name='department_id',
            new_name='department',
        ),
    ]