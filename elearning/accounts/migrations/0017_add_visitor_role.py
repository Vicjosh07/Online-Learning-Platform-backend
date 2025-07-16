# accounts/migrations/0017_add_visitor_role.py
from django.db import migrations, models

def add_visitor_role(apps, schema_editor):
    UserProfile = apps.get_model('accounts', 'UserProfile')
    # No need to update existing records - just adding a new option

class Migration(migrations.Migration):
    dependencies = [
        ('accounts', '0016_set_default_roles'),  # Your last migration
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='role',
            field=models.CharField(
                choices=[
                    ('VISITOR', 'Visitor'),
                    ('STUDENT', 'Student'),
                    ('LECTURER', 'Lecturer')
                ],
                default='VISITOR',  # Or keep as 'STUDENT' if preferred
                max_length=10
            ),
        ),
        migrations.RunPython(add_visitor_role),
    ]