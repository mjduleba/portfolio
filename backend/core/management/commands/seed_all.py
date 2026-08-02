from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Seed all models with initial portfolio data'

    def handle(self, *args, **options):
        call_command('seed_profile')
        call_command('seed_skills')
        call_command('seed_experience')
        call_command('seed_projects')
        call_command('seed_tools')
        self.stdout.write(self.style.SUCCESS('All seeding complete.'))
