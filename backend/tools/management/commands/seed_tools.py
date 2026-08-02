from django.core.management.base import BaseCommand

from tools.models import Tool


class Command(BaseCommand):
    help = 'Seed the Tool model with initial data'

    def handle(self, *args, **options):
        tools = [
            {
                'title': 'Skills & Agents Showcase',
                'slug': 'skills-agents',
                'category': Tool.Category.TOOL,
                'description': (
                    "A collection of the custom Claude Code skills and subagents I've built and used."
                    "\n\n"
                    "Each entry walks through the purpose of the skill/subagent, usage examples, "
                    "and how it fits into a real development loop."
                ),
                'url': '',  # TODO: insert real repo URL once the showcase repo is created
                'order': 0,
            },
        ]
        for t in tools:
            Tool.objects.update_or_create(slug=t['slug'], defaults=t)
        self.stdout.write(self.style.SUCCESS('Tools seeded.'))
