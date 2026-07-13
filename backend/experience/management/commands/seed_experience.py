from django.core.management.base import BaseCommand

from experience.models import Experience


class Command(BaseCommand):
    help = 'Seed the Experience model with initial data'

    def handle(self, *args, **options):
        entries = [
            {
                'role': 'Software Developer',
                'company': 'Cohen and Co.',
                'location': 'Cleveland, OH',
                'start_date': '2023-01-01',
                'end_date': None,
                'bullets': [
                    'Spearheaded development of an audit workpaper automation platform using Python, FastAPI, and Vue.js, eliminating 20,000+ hours of manual workpaper conversions annually.',
                    'Crafted over a dozen audit report conversion services using Python and external integrations to normalize financial data and automate workpaper generation for 1,000+ funds annually.',
                    'Developed Vue.js frontend orchestrating multi-step user workflows that coordinated sequential endpoint calls to submit, validate, and retrieve workpaper outputs.',
                    'Built and maintained a pytest-driven test suite with unit tests for core conversion logic and integration tests against mocked market data APIs to catch regressions before deployment.',
                    'Decoupled workpaper conversion processing from the FastAPI web layer using RabbitMQ, offloading long-running jobs to distributed worker consumers to eliminate request timeouts across 100,000+ record submissions.',
                    'Designed a multi-container Docker architecture orchestrating client, server, and RabbitMQ containers into a unified startup workflow ensuring consistency across environments.',
                    'Established onboarding and code review standards for junior developers, translating architectural decisions into actionable guidance that elevated team code quality.',
                ],
            },
        ]
        for e in entries:
            Experience.objects.get_or_create(
                role=e['role'],
                company=e['company'],
                defaults=e,
            )
        self.stdout.write(self.style.SUCCESS('Experience seeded.'))
