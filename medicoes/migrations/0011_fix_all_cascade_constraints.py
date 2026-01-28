# Generated migration to fix CASCADE constraints in all FK tables

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicoes', '0010_fix_usuario_cascade_sqlite'),
    ]

    operations = [
        migrations.RunSQL(
            """
            -- Fix medicoes_customuser_groups table
            CREATE TABLE medicoes_customuser_groups_new (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                customuser_id BIGINT NOT NULL,
                group_id INTEGER NOT NULL,
                FOREIGN KEY (customuser_id) REFERENCES medicoes_customuser(id) ON DELETE CASCADE,
                FOREIGN KEY (group_id) REFERENCES auth_group(id) ON DELETE CASCADE
            );
            
            INSERT INTO medicoes_customuser_groups_new
            SELECT id, customuser_id, group_id FROM medicoes_customuser_groups;
            
            DROP TABLE medicoes_customuser_groups;
            ALTER TABLE medicoes_customuser_groups_new RENAME TO medicoes_customuser_groups;
            
            -- Fix medicoes_customuser_areas table
            CREATE TABLE medicoes_customuser_areas_new (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                customuser_id BIGINT NOT NULL,
                areaofexpertise_id BIGINT NOT NULL,
                FOREIGN KEY (customuser_id) REFERENCES medicoes_customuser(id) ON DELETE CASCADE,
                FOREIGN KEY (areaofexpertise_id) REFERENCES medicoes_areaofexpertise(id) ON DELETE CASCADE
            );
            
            INSERT INTO medicoes_customuser_areas_new
            SELECT id, customuser_id, areaofexpertise_id FROM medicoes_customuser_areas;
            
            DROP TABLE medicoes_customuser_areas;
            ALTER TABLE medicoes_customuser_areas_new RENAME TO medicoes_customuser_areas;
            
            -- Fix medicoes_customuser_user_permissions table
            CREATE TABLE medicoes_customuser_user_permissions_new (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                customuser_id BIGINT NOT NULL,
                permission_id INTEGER NOT NULL,
                FOREIGN KEY (customuser_id) REFERENCES medicoes_customuser(id) ON DELETE CASCADE,
                FOREIGN KEY (permission_id) REFERENCES auth_permission(id) ON DELETE CASCADE
            );
            
            INSERT INTO medicoes_customuser_user_permissions_new
            SELECT id, customuser_id, permission_id FROM medicoes_customuser_user_permissions;
            
            DROP TABLE medicoes_customuser_user_permissions;
            ALTER TABLE medicoes_customuser_user_permissions_new RENAME TO medicoes_customuser_user_permissions;
            
            -- Fix django_admin_log table (for regular auth_user)
            CREATE TABLE django_admin_log_new (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                action_time DATETIME NOT NULL,
                user_id INTEGER NOT NULL,
                content_type_id INTEGER NOT NULL,
                object_id TEXT,
                object_repr VARCHAR(200) NOT NULL,
                action_flag SMALLINT NOT NULL,
                change_message TEXT NOT NULL,
                FOREIGN KEY (user_id) REFERENCES auth_user(id) ON DELETE CASCADE,
                FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) ON DELETE CASCADE
            );
            
            INSERT INTO django_admin_log_new
            SELECT id, action_time, user_id, content_type_id, object_id, object_repr, action_flag, change_message 
            FROM django_admin_log;
            
            DROP TABLE django_admin_log;
            ALTER TABLE django_admin_log_new RENAME TO django_admin_log;
            """,
            """
            -- Reverse: recreate tables with NO ACTION constraints
            CREATE TABLE medicoes_customuser_groups_new (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                customuser_id BIGINT NOT NULL,
                group_id INTEGER NOT NULL,
                FOREIGN KEY (customuser_id) REFERENCES medicoes_customuser(id) ON DELETE NO ACTION,
                FOREIGN KEY (group_id) REFERENCES auth_group(id) ON DELETE NO ACTION
            );
            
            INSERT INTO medicoes_customuser_groups_new
            SELECT id, customuser_id, group_id FROM medicoes_customuser_groups;
            
            DROP TABLE medicoes_customuser_groups;
            ALTER TABLE medicoes_customuser_groups_new RENAME TO medicoes_customuser_groups;
            
            CREATE TABLE medicoes_customuser_areas_new (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                customuser_id BIGINT NOT NULL,
                areaofexpertise_id BIGINT NOT NULL,
                FOREIGN KEY (customuser_id) REFERENCES medicoes_customuser(id) ON DELETE NO ACTION,
                FOREIGN KEY (areaofexpertise_id) REFERENCES medicoes_areaofexpertise(id) ON DELETE NO ACTION
            );
            
            INSERT INTO medicoes_customuser_areas_new
            SELECT id, customuser_id, areaofexpertise_id FROM medicoes_customuser_areas;
            
            DROP TABLE medicoes_customuser_areas;
            ALTER TABLE medicoes_customuser_areas_new RENAME TO medicoes_customuser_areas;
            
            CREATE TABLE medicoes_customuser_user_permissions_new (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                customuser_id BIGINT NOT NULL,
                permission_id INTEGER NOT NULL,
                FOREIGN KEY (customuser_id) REFERENCES medicoes_customuser(id) ON DELETE NO ACTION,
                FOREIGN KEY (permission_id) REFERENCES auth_permission(id) ON DELETE NO ACTION
            );
            
            INSERT INTO medicoes_customuser_user_permissions_new
            SELECT id, customuser_id, permission_id FROM medicoes_customuser_user_permissions;
            
            DROP TABLE medicoes_customuser_user_permissions;
            ALTER TABLE medicoes_customuser_user_permissions_new RENAME TO medicoes_customuser_user_permissions;
            
            CREATE TABLE django_admin_log_new (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                action_time DATETIME NOT NULL,
                user_id INTEGER NOT NULL,
                content_type_id INTEGER NOT NULL,
                object_id TEXT,
                object_repr VARCHAR(200) NOT NULL,
                action_flag SMALLINT NOT NULL,
                change_message TEXT NOT NULL,
                FOREIGN KEY (user_id) REFERENCES auth_user(id) ON DELETE NO ACTION,
                FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) ON DELETE NO ACTION
            );
            
            INSERT INTO django_admin_log_new
            SELECT id, action_time, user_id, content_type_id, object_id, object_repr, action_flag, change_message 
            FROM django_admin_log;
            
            DROP TABLE django_admin_log;
            ALTER TABLE django_admin_log_new RENAME TO django_admin_log;
            """
        ),
    ]
