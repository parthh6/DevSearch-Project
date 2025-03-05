# Generated by Django 5.0.6 on 2025-03-05 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_profile_options_alter_profile_short_intro_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='location',
            field=models.CharField(blank=True, default='Earth', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='username',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
