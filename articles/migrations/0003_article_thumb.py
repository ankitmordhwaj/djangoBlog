# Generated by Django 4.1.4 on 2023-01-04 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_rename_titile_article_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='thumb',
            field=models.ImageField(blank=True, default='default.png', upload_to=''),
        ),
    ]
