from django.db import migrations

def set_default_roles(apps, schema_editor):
    UserProfile = apps.get_model('accounts', 'UserProfile')
    UserProfile.objects.filter(role__isnull=True).update(role='STUDENT')

class Migration(migrations.Migration):
    dependencies = [
        ('accounts', '0015_add_role_field'),
    ]

    operations = [
        migrations.RunPython(set_default_roles),
    ]