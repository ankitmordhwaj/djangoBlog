# Generated by Django 4.1.4 on 2022-12-20 11:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='titile',
            new_name='title',
        ),
    ]
