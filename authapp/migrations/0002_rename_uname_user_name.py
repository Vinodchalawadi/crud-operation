# Generated by Django 4.1.3 on 2022-12-07 06:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='uname',
            new_name='name',
        ),
    ]
