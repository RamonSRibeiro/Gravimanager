# Generated migration to restore auth_user data from medicoes_customuser

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicoes', '0011_fix_all_cascade_constraints'),
    ]

    operations = [
        migrations.RunSQL(
            """
            -- Restaurar dados de auth_user a partir de medicoes_customuser
            INSERT INTO auth_user (
                id, password, last_login, is_superuser, username, first_name, 
                last_name, email, is_staff, is_active, date_joined
            )
            SELECT 
                cu.id, cu.password, cu.last_login, cu.is_superuser, cu.username,
                cu.first_name, cu.last_name, cu.email, cu.is_staff, cu.is_active,
                cu.date_joined
            FROM medicoes_customuser cu
            WHERE cu.id NOT IN (SELECT id FROM auth_user);
            """,
            """
            -- Reverse: remover registros adicionados
            DELETE FROM auth_user WHERE id IN (
                SELECT cu.id FROM medicoes_customuser cu
            ) AND id NOT IN (
                SELECT user_ptr_id FROM medicoes_customuser
            );
            """
        ),
    ]
