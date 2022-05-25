# Generated by Django 4.0.4 on 2022-05-21 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ajaxapp', '0002_rename_ajaxcrud_student_alter_student_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='Email',
        ),
        migrations.RemoveField(
            model_name='student',
            name='Name',
        ),
        migrations.RemoveField(
            model_name='student',
            name='Password',
        ),
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.CharField(default=1, max_length=20, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='name',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='passwd',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
