from django.core.management.base import BaseCommand

from tools.models import Tool, SkillAgentEntry


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
                'url': '',
                'order': 0,
                'skill_agent_entries': [],
            },
        ]
        for t in tools:
            entries = t.pop('skill_agent_entries')
            tool, _ = Tool.objects.update_or_create(slug=t['slug'], defaults=t)
            tool.skill_agent_entries.all().delete()
            for i, e in enumerate(entries):
                SkillAgentEntry.objects.create(
                    tool=tool, name=e['name'], kind=e['kind'], description=e['description'],
                    tags=e.get('tags', []), video_url=e.get('video_url', ''),
                    image_url=e.get('image_url', ''), order=i,
                )
        self.stdout.write(self.style.SUCCESS('Tools seeded.'))
