# Generated by Django 1.10.2 on 2016-10-16 08:55
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0006_auto_20160623_1627'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'default_manager_name': 'objects', 'verbose_name': 'image', 'verbose_name_plural': 'images'},
        ),
    ]