from mongoengine import connect

# Connect to MongoDB
connect(db="octofit_db", host="localhost", port=27017)

from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        # Drop existing collections
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create users
        user1 = User(email='thundergod@mhigh.edu', name='Thundergod', password='thundergodpassword').save()
        user2 = User(email='metalgeek@mhigh.edu', name='Metalgeek', password='metalgeekpassword').save()
        user3 = User(email='zerocool@mhigh.edu', name='Zerocool', password='zerocoolpassword').save()
        user4 = User(email='crashoverride@hmhigh.edu', name='Crashoverride', password='crashoverridepassword').save()
        user5 = User(email='sleeptoken@mhigh.edu', name='Sleeptoken', password='sleeptokenpassword').save()

        # Create teams
        team1 = Team(name='Team Asgard', members=[user1, user2]).save()
        team2 = Team(name='Team Midgard', members=[user3, user4, user5]).save()

        # Create activities
        Activity(user=user1, activity_type='Running', duration=30, date='2025-04-20').save()
        Activity(user=user2, activity_type='Cycling', duration=45, date='2025-04-19').save()
        Activity(user=user3, activity_type='Swimming', duration=60, date='2025-04-21').save()
        Activity(user=user4, activity_type='Hiking', duration=120, date='2025-04-18').save()
        Activity(user=user5, activity_type='Yoga', duration=90, date='2025-04-17').save()

        # Create leaderboard entries
        Leaderboard(user=user1, score=100).save()
        Leaderboard(user=user2, score=80).save()
        Leaderboard(user=user3, score=120).save()
        Leaderboard(user=user4, score=200).save()
        Leaderboard(user=user5, score=170).save()

        # Create workouts
        Workout(name='Morning Run', description='A quick morning run to start the day', duration=30).save()
        Workout(name='Evening Yoga', description='Relaxing yoga session', duration=45).save()
        Workout(name='HIIT', description='High-intensity interval training', duration=30).save()
        Workout(name='Swimming Laps', description='Endurance swimming', duration=60).save()
        Workout(name='Mountain Hike', description='Challenging hike in the mountains', duration=120).save()

        self.stdout.write(self.style.SUCCESS('Test data successfully populated in the database.'))
