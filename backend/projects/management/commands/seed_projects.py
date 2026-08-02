from django.core.management.base import BaseCommand

from projects.models import Project, ProjectBullet


class Command(BaseCommand):
    help = 'Seed the Project model with initial data'

    def handle(self, *args, **options):
        projects = [
            {
                'title': 'Game Insights Bot',
                'description': (
                    'An asynchronous data pipeline that retrieves MLB schedules, player statistics, and team lineups '
                    'from the official MLB Stats API and delivers real-time sports data via a Discord bot using slash commands.'
                ),
                'tech_stack': ['Python', 'FastAPI', 'AWS', 'REST API'],
                'github_url': 'https://github.com/mjduleba/betting-insight-bot',
                'demo_url': None,
                'video_url': '',  # TODO: insert real video URL once available
                'image_url': '',  # TODO: insert real screenshot URL once available
                'featured': True,
                'order': 2,
                'bullets': [
                    {
                        'text': 
                            'Applied a sport-first modular Python layout separating shared infrastructure  '
                            'from sport-specific logic, making it considerably easier to add new sports', 
                        'tags': ['Python']
                    },
                    {
                        'text': 
                            'Aggregated multiple third-party data API Integrations into a single '
                            'unified response to build one cohesive Discord embed per user request',
                        'tags': ['API Integrations']
                    },
                    {
                        'text': 
                            'Implemented Data Validation by modeling domain data with immutable, slotted dataclasses for request/response objects, '
                            'giving predictable equality, reduced memory overhead, and preventing accidental mutation of snapshot data mid-request',
                        'tags': ['Data Validation']
                    }
                ],
            },
            # {
            #     'title': 'Health Data Pipeline',
            #     'description': (
            #         'A cloud-based health analytics platform on AWS that ingests, processes, and analyzes '
            #         'wearable data via the WHOOP API, enabling centralized tracking of health metrics for weekly insights.'
            #     ),
            #     'tech_stack': ['Python', 'FastAPI', 'PostgreSQL', 'AWS', 'REST API'],
            #     'github_url': 'https://github.com/mjduleba/health-analysis-summary',
            #     'demo_url': None,
            #     'video_url': '',  # TODO: insert real video URL once available
            #     'image_url': '',  # TODO: insert real screenshot URL once available
            #     'featured': True,
            #     'order': 1,
            #     'bullets': [
            #         {'text': 
            #             'Designed and built an ELT pipeline ingesting biometric and nutrition data '
            #             'from two third-party data API Integrations into a normalized PostgreSQL '
            #             'warehouse for downstream analytics', 
            #         'tags': ['ETL Pipelines', 'API Integrations', 'PostgreSQL']
            #         },
            #         {'text': 
            #             'Containerized PostgreSQL via Docker Compose with health checks, named volumes '
            #             'for data persistence, and .env-driven configuration for local reproducible development', 
            #         'tags': ['PostgreSQL', 'Docker']
            #         },
            #         {'text': 
            #             'Implemented OAuth 2.0 authorization-code flow for third-party API authentication', 
            #         'tags': ['OAuth']
            #         },
            #     ],
            # },
        ]
        for p in projects:
            bullets = p.pop('bullets')
            proj, _ = Project.objects.update_or_create(title=p['title'], defaults=p)
            proj.bullets.all().delete()
            for i, b in enumerate(bullets):
                ProjectBullet.objects.create(project=proj, text=b['text'], tags=b['tags'], order=i)
        self.stdout.write(self.style.SUCCESS('Projects seeded.'))
