# Generated by Django 5.1.7 on 2025-03-13 02:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_course_description_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Course',
        ),
    ]
