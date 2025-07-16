from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [
        ('accounts', '0014_alter_userprofile_facebook_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='role',
            field=models.CharField(
                choices=[('STUDENT', 'Student'), ('LECTURER', 'Lecturer'), ('ADMIN', 'Administrator')],
                default='STUDENT',
                max_length=10
            ),
        ),
    ]