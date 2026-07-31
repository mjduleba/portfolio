from django.core.management.base import BaseCommand

from userprofile.models import Education, UserProfile


class Command(BaseCommand):
    help = 'Seed the UserProfile model with initial data'

    def handle(self, *args, **options):
        profile, _ = UserProfile.objects.get_or_create(
            email='michael.duleba1@gmail.com',
            defaults={
                'name': 'Michael Duleba',
                'title': 'Software Developer',
                'bio': (
                    'Software developer at Cohen and Co. building backend systems, data pipelines, '
                    'and automation tools with Python, FastAPI, and Django. '
                    'B.S. in Computer Science from Cleveland State University.'
                ),
                'github_url': 'https://github.com/mjduleba',
                'linkedin_url': 'https://linkedin.com/in/michael-duleba',
                'location': 'Cleveland, Ohio',
            }
        )

        Education.objects.get_or_create(
            profile=profile,
            institution='Cleveland State University',
            degree='B.S. in Computer Science',
            defaults={
                'institution_icon_key': 'cleveland-state',
                'degree_icon_key': 'graduation-cap',
                'order': 0,
            }
        )

        self.stdout.write(self.style.SUCCESS('UserProfile seeded.'))
