from django.core.management.base import BaseCommand

from skills.models import Skill


class Command(BaseCommand):
    help = 'Seed the Skill model with initial data'

    def handle(self, *args, **options):
        skills = [
            # Languages & Querying
            {'name': 'Python', 'category': Skill.Category.LANGUAGES, 'order': 1, 'icon_key': 'python'},
            {'name': 'JavaScript', 'category': Skill.Category.LANGUAGES, 'order': 2, 'icon_key': 'javascript'},
            {'name': 'TypeScript', 'category': Skill.Category.LANGUAGES, 'order': 3, 'icon_key': 'typescript'},
            {'name': 'Java', 'category': Skill.Category.LANGUAGES, 'order': 4, 'icon_key': 'java'},
            {'name': 'SQL', 'category': Skill.Category.LANGUAGES, 'order': 5, 'icon_key': 'sql'},
            {'name': 'CSS', 'category': Skill.Category.LANGUAGES, 'order': 6, 'icon_key': 'css'},

            # Frameworks, Libraries & Tools
            {'name': 'FastAPI', 'category': Skill.Category.FRAMEWORKS, 'order': 1, 'icon_key': 'fastapi'},
            {'name': 'Django', 'category': Skill.Category.FRAMEWORKS, 'order': 2, 'icon_key': 'django'},
            {'name': 'Vue.js', 'category': Skill.Category.FRAMEWORKS, 'order': 3, 'icon_key': 'vuejs'},
            {'name': 'React', 'category': Skill.Category.FRAMEWORKS, 'order': 4, 'icon_key': 'react'},
            {'name': 'RabbitMQ', 'category': Skill.Category.FRAMEWORKS, 'order': 5, 'icon_key': 'rabbitmq'},
            {'name': 'PostgreSQL', 'category': Skill.Category.FRAMEWORKS, 'order': 6, 'icon_key': 'postgresql'},
            {'name': 'Pandas', 'category': Skill.Category.FRAMEWORKS, 'order': 7, 'icon_key': 'pandas'},
            {'name': 'Git', 'category': Skill.Category.FRAMEWORKS, 'order': 8, 'icon_key': 'git'},
            {'name': 'Postman', 'category': Skill.Category.FRAMEWORKS, 'order': 9, 'icon_key': 'postman'},
            {'name': 'Grafana', 'category': Skill.Category.FRAMEWORKS, 'order': 10, 'icon_key': 'grafana'},

            # Cloud & Infrastructure
            {'name': 'Docker', 'category': Skill.Category.CLOUD, 'order': 1, 'icon_key': 'docker'},
            {'name': 'Jenkins', 'category': Skill.Category.CLOUD, 'order': 2, 'icon_key': 'jenkins'},
            {'name': 'AWS', 'category': Skill.Category.CLOUD, 'order': 3, 'icon_key': 'aws'},
            {'name': 'Bitbucket', 'category': Skill.Category.CLOUD, 'order': 4, 'icon_key': 'bitbucket'},
            {'name': 'GitHub', 'category': Skill.Category.CLOUD, 'order': 5, 'icon_key': 'github'},

            # Technical Concepts
            {'name': 'API Integration', 'category': Skill.Category.CONCEPTS, 'order': 1, 'icon_key': ''},
            {'name': 'ETL Pipelines', 'category': Skill.Category.CONCEPTS, 'order': 2, 'icon_key': ''},
            {'name': 'Data Validation', 'category': Skill.Category.CONCEPTS, 'order': 3, 'icon_key': ''},
            {'name': 'Workflow Automation', 'category': Skill.Category.CONCEPTS, 'order': 4, 'icon_key': ''},
            {'name': 'Pub/Sub Patterns', 'category': Skill.Category.CONCEPTS, 'order': 5, 'icon_key': ''},
            {'name': 'Asynchronous Processing', 'category': Skill.Category.CONCEPTS, 'order': 6, 'icon_key': ''},
            {'name': 'OAuth', 'category': Skill.Category.CONCEPTS, 'order': 7, 'icon_key': ''},
            {'name': 'Azure MSAL Authentication', 'category': Skill.Category.CONCEPTS, 'order': 8, 'icon_key': ''},
            {'name': 'REST API Design', 'category': Skill.Category.CONCEPTS, 'order': 9, 'icon_key': ''},
            {'name': 'CI/CD Pipelines', 'category': Skill.Category.CONCEPTS, 'order': 10, 'icon_key': ''},
        ]
        for s in skills:
            Skill.objects.update_or_create(name=s['name'], defaults=s)
        self.stdout.write(self.style.SUCCESS('Skills seeded.'))
