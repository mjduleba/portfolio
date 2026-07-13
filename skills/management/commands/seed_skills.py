from django.core.management.base import BaseCommand

from skills.models import Skill


class Command(BaseCommand):
    help = 'Seed the Skill model with initial data'

    def handle(self, *args, **options):
        skills = [
            # Languages & Querying
            {'name': 'Python', 'category': Skill.Category.LANGUAGES, 'order': 1},
            {'name': 'JavaScript', 'category': Skill.Category.LANGUAGES, 'order': 2},
            {'name': 'TypeScript', 'category': Skill.Category.LANGUAGES, 'order': 3},
            {'name': 'Java', 'category': Skill.Category.LANGUAGES, 'order': 4},
            {'name': 'SQL', 'category': Skill.Category.LANGUAGES, 'order': 5},
            {'name': 'CSS', 'category': Skill.Category.LANGUAGES, 'order': 6},
            {'name': 'Bash', 'category': Skill.Category.LANGUAGES, 'order': 7},

            # Frameworks, Libraries & Tools
            {'name': 'FastAPI', 'category': Skill.Category.FRAMEWORKS, 'order': 1},
            {'name': 'Django', 'category': Skill.Category.FRAMEWORKS, 'order': 2},
            {'name': 'Vue.js', 'category': Skill.Category.FRAMEWORKS, 'order': 3},
            {'name': 'React', 'category': Skill.Category.FRAMEWORKS, 'order': 4},
            {'name': 'RabbitMQ', 'category': Skill.Category.FRAMEWORKS, 'order': 5},
            {'name': 'PostgreSQL', 'category': Skill.Category.FRAMEWORKS, 'order': 6},
            {'name': 'Pandas', 'category': Skill.Category.FRAMEWORKS, 'order': 7},
            {'name': 'Git', 'category': Skill.Category.FRAMEWORKS, 'order': 8},
            {'name': 'Postman', 'category': Skill.Category.FRAMEWORKS, 'order': 9},
            {'name': 'Grafana', 'category': Skill.Category.FRAMEWORKS, 'order': 10},

            # Cloud & Infrastructure
            {'name': 'Docker', 'category': Skill.Category.CLOUD, 'order': 1},
            {'name': 'REST API Design', 'category': Skill.Category.CLOUD, 'order': 2},
            {'name': 'CI/CD Pipelines', 'category': Skill.Category.CLOUD, 'order': 3},
            {'name': 'Jenkins', 'category': Skill.Category.CLOUD, 'order': 4},
            {'name': 'AWS EC2', 'category': Skill.Category.CLOUD, 'order': 5},
            {'name': 'AWS S3', 'category': Skill.Category.CLOUD, 'order': 6},
            {'name': 'AWS RDS', 'category': Skill.Category.CLOUD, 'order': 7},

            # Technical Concepts
            {'name': 'API Integration', 'category': Skill.Category.CONCEPTS, 'order': 1},
            {'name': 'ETL Pipelines', 'category': Skill.Category.CONCEPTS, 'order': 2},
            {'name': 'Data Validation', 'category': Skill.Category.CONCEPTS, 'order': 3},
            {'name': 'Workflow Automation', 'category': Skill.Category.CONCEPTS, 'order': 4},
            {'name': 'Pub/Sub Patterns', 'category': Skill.Category.CONCEPTS, 'order': 5},
            {'name': 'Asynchronous Processing', 'category': Skill.Category.CONCEPTS, 'order': 6},
            {'name': 'OAuth', 'category': Skill.Category.CONCEPTS, 'order': 7},
            {'name': 'Azure MSAL Authentication', 'category': Skill.Category.CONCEPTS, 'order': 8},
        ]
        for s in skills:
            Skill.objects.get_or_create(name=s['name'], defaults=s)
        self.stdout.write(self.style.SUCCESS('Skills seeded.'))
