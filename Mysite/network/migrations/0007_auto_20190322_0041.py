# Generated by Django 2.1.5 on 2019-03-21 19:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0006_auto_20190322_0004'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='cover_image',
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_cover',
            field=models.ImageField(default='cover_pic.jpg', upload_to='cover_pics'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(default='profile_pic.jpg', upload_to='profile_pics'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]