"""
Management command para popular as áreas de atuação no banco de dados
Uso: python manage.py populate_areas
"""

from django.core.management.base import BaseCommand
from medicoes.models import AreaOfExpertise
from medicoes.category_config import EXPERTISE_AREAS


class Command(BaseCommand):
    help = 'Popula a tabela AreaOfExpertise com data de expertise_areas'

    def add_arguments(self, parser):
        parser.add_argument(
            '--clear',
            action='store_true',
            help='Limpar áreas existentes antes de popular',
        )

    def handle(self, *args, **options):
        if options['clear']:
            count = AreaOfExpertise.objects.count()
            AreaOfExpertise.objects.all().delete()
            self.stdout.write(
                self.style.SUCCESS(f'✓ Removidas {count} áreas existentes')
            )

        created_count = 0
        for key, data in EXPERTISE_AREAS.items():
            area, created = AreaOfExpertise.objects.get_or_create(
                key=key,
                defaults={'label': data['label']}
            )
            if created:
                created_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f'✓ Criada área: {area.label}')
                )
            else:
                # Atualizar label se mudou
                if area.label != data['label']:
                    area.label = data['label']
                    area.save()
                    self.stdout.write(
                        self.style.WARNING(f'✓ Atualizada área: {area.label}')
                    )
                else:
                    self.stdout.write(
                        self.style.SUCCESS(f'✓ Área existente: {area.label}')
                    )

        total = AreaOfExpertise.objects.count()
        self.stdout.write(
            self.style.SUCCESS(
                f'\n✓ Total de áreas cadastradas: {total} '
                f'({created_count} novas)'
            )
        )
