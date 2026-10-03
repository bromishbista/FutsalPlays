"""Load demo data so the project can be explored after a fresh install.

Usage:  python manage.py seed_demo
Creates the futsal venues and blog posts, a demo player account, two teams,
one upcoming match and a chat group.
"""
from datetime import timedelta, time

from django.contrib.auth.models import User
from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.utils import timezone

from booking.models import Futsal, Match, Team
from groupchat.models import UserGroups


class Command(BaseCommand):
    help = "Load demo venues, users, teams and a match"

    def handle(self, *args, **options):
        call_command("loaddata", "demo_content.json")

        demo, created = User.objects.get_or_create(
            username="demo", defaults={"email": "demo@example.com", "first_name": "Demo"}
        )
        if created:
            demo.set_password("demo12345")
            demo.save()
        rival, created = User.objects.get_or_create(
            username="rival", defaults={"email": "rival@example.com", "first_name": "Rival"}
        )
        if created:
            rival.set_password("demo12345")
            rival.save()

        now = timezone.now()
        wolves, _ = Team.objects.get_or_create(
            name="Wolves",
            defaults=dict(user=demo, team_image="img/team.png", location="Boudha, Kathmandu",
                          join_date=now, players=7),
        )
        bangers, _ = Team.objects.get_or_create(
            name="Bangers",
            defaults=dict(user=rival, team_image="img/team.png", location="Sankhamul, Kathmandu",
                          join_date=now, players=6),
        )
        venue = Futsal.objects.order_by("id").first()
        Match.objects.get_or_create(
            first_team=wolves, second_team=bangers,
            defaults=dict(futsal=venue, date=now + timedelta(days=3),
                          first_image="img/team.png", second_image="img/team.png",
                          start_time=time(18, 0), end_time=time(19, 0),
                          playercount="7", gametype="friendly match"),
        )
        group, _ = UserGroups.objects.get_or_create(group_name="Friday Night Futsal")
        group.members.add(demo, rival)

        self.stdout.write(self.style.SUCCESS(
            "Demo data loaded. Log in with username 'demo' and password 'demo12345'."
        ))
