# Generated by Django 4.0.4 on 2022-05-20 09:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Ajaxapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AjaxCrud',
            new_name='Student',
        ),
        migrations.AlterModelTable(
            name='student',
            table='student',
        ),
    ]
