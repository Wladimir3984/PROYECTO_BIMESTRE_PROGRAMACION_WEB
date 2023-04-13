from django.db import migrations
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User

def create_permission(apps, schema_editor):
    # Get the content type for the user model
    content_type = ContentType.objects.get_for_model(User)
    # Create the permission
    permissionUser = Permission.objects.create(
        codename='rol_user',
        name='Can view/use the common user page',
        content_type=content_type,
    )

    permissionSupervisor = Permission.objects.create(
        codename='rol_supervisor',
        name='Have acces to the custom admin panel',
        content_type=content_type,
    )

class Migration(migrations.Migration):

    dependencies = [('app', '0003_insert_data'),
    ]

    operations = [
        migrations.RunPython(create_permission),
    ]
