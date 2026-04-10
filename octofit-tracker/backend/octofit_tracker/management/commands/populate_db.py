from django.core.management.base import BaseCommand
from django.conf import settings
from djongo import models

# Placeholder models for demonstration; replace with actual models if defined
from octofit_tracker import models as octo_models

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        octo_models.User.objects.all().delete()
        octo_models.Team.objects.all().delete()
        octo_models.Activity.objects.all().delete()
        octo_models.Leaderboard.objects.all().delete()
        octo_models.Workout.objects.all().delete()

        # Create Teams
        marvel = octo_models.Team.objects.create(name='Team Marvel')
        dc = octo_models.Team.objects.create(name='Team DC')

        # Create Users
        ironman = octo_models.User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel)
        captain = octo_models.User.objects.create(name='Captain America', email='cap@marvel.com', team=marvel)
        batman = octo_models.User.objects.create(name='Batman', email='batman@dc.com', team=dc)
        superman = octo_models.User.objects.create(name='Superman', email='superman@dc.com', team=dc)

        # Create Activities
        octo_models.Activity.objects.create(user=ironman, type='run', duration=30)
        octo_models.Activity.objects.create(user=batman, type='cycle', duration=45)

        # Create Workouts
        octo_models.Workout.objects.create(user=ironman, description='Chest day', duration=60)
        octo_models.Workout.objects.create(user=superman, description='Leg day', duration=50)

        # Create Leaderboard
        octo_models.Leaderboard.objects.create(user=ironman, points=100)
        octo_models.Leaderboard.objects.create(user=batman, points=90)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
