# Generated by Django 5.1.7 on 2025-03-13 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_alter_userprofile_facebook_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='occupation',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='facebook',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='linkedin',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
