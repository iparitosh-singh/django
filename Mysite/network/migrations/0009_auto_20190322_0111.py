# Generated by Django 2.1.5 on 2019-03-21 19:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0008_auto_20190322_0105'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='profile_image',
            new_name='image',
        ),
    ]
