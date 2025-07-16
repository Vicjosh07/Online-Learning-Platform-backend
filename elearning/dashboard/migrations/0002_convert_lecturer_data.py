from django.db import migrations


def create_lecturer_users(apps, schema_editor):
    Course = apps.get_model('dashboard', 'Course')
    User = apps.get_model('auth', 'User')
    UserProfile = apps.get_model('accounts', 'UserProfile')

    for course in Course.objects.filter(lecturer__isnull=False):
        try:
            # Skip if lecturer is already a User instance
            if isinstance(course.lecturer, User):
                continue

            # Create new lecturer user
            username = course.lecturer.lower().replace(' ', '_')
            user, created = User.objects.get_or_create(
                username=username,
                defaults={
                    'first_name': course.lecturer.split(' ')[0],
                    'last_name': ' '.join(course.lecturer.split(' ')[1:]),
                    'is_active': True
                }
            )

            # Ensure UserProfile exists
            UserProfile.objects.get_or_create(
                user=user,
                defaults={'role': 'LECTURER'}
            )

            course.lecturer = user
            course.save()
        except Exception as e:
            print(f"Error processing course {course.id}: {e}")


class Migration(migrations.Migration):
    dependencies = [
        ('dashboard', '0001_initial'),  # Your initial migration
        ('accounts', '0016_set_default_roles'),
    ]

    operations = [
        migrations.RunPython(create_lecturer_users),
    ]