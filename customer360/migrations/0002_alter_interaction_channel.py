# Generated by Django 5.1.4 on 2025-01-01 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer360', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interaction',
            name='channel',
            field=models.CharField(choices=[('phone', 'Phone'), ('sms', 'SMS'), ('email', 'Email'), ('letter', 'Letter'), ('social_media', 'social_media')], max_length=15),
        ),
    ]