from django.core.management.base import BaseCommand

from projects.models import Project


class Command(BaseCommand):
    help = 'Seed the Project model with initial data'

    def handle(self, *args, **options):
        projects = [
            {
                'title': 'Health Data Pipeline',
                'description': (
                    'A cloud-based health analytics platform on AWS that ingests, processes, and analyzes '
                    'wearable data via the WHOOP API, enabling centralized tracking of health metrics for weekly insights.'
                ),
                'tech_stack': ['Python', 'FastAPI', 'PostgreSQL', 'AWS', 'REST API', 'Requests'],
                'github_url': 'https://github.com/mjduleba/TODO',
                'demo_url': None,
                'featured': True,
                'order': 1,
            },
            {
                'title': 'Game Insights Bot',
                'description': (
                    'An asynchronous data pipeline that retrieves MLB schedules, player statistics, and team lineups '
                    'from the official MLB Stats API and delivers real-time sports data via a Discord bot using slash commands.'
                ),
                'tech_stack': ['Python', 'FastAPI', 'AWS EC2', 'REST API', 'HTTPX', 'Pydantic'],
                'github_url': 'https://github.com/mjduleba/TODO',
                'demo_url': None,
                'featured': True,
                'order': 2,
            },
        ]
        for p in projects:
            Project.objects.get_or_create(title=p['title'], defaults=p)
        self.stdout.write(self.style.SUCCESS('Projects seeded.'))
