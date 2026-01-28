# Generated migration to populate AreaOfExpertise

from django.db import migrations


def populate_expertise_areas(apps, schema_editor):
    """Popula as áreas de expertise predefinidas"""
    AreaOfExpertise = apps.get_model('medicoes', 'AreaOfExpertise')
    
    areas = [
        ('geosciences', 'Geociências'),
        ('metrology', 'Metrologia'),
        ('physics', 'Física'),
        ('defense', 'Defesa'),
        ('science_communication', 'Divulgação Científica'),
    ]
    
    for key, label in areas:
        AreaOfExpertise.objects.get_or_create(
            key=key,
            defaults={'label': label}
        )


def reverse_populate(apps, schema_editor):
    """Remove as áreas de expertise"""
    AreaOfExpertise = apps.get_model('medicoes', 'AreaOfExpertise')
    AreaOfExpertise.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('medicoes', '0007_areaofexpertise_customuser_role_category_and_more'),
    ]

    operations = [
        migrations.RunPython(populate_expertise_areas, reverse_populate),
    ]
