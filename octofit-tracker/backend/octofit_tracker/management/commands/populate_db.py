from mongoengine import connect

# Connect to MongoDB
connect(db="octofit_db", host="localhost", port=27017)

from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        # Create test users
        user1 = User(email='user1@example.com', name='User One', password='password1').save()
        user2 = User(email='user2@example.com', name='User Two', password='password2').save()

        # Create test teams
        team1 = Team(name='Team Alpha', members=[user1, user2]).save()

        # Create test activities
        Activity(user=user1, activity_type='Running', duration=30, date='2025-04-20').save()
        Activity(user=user2, activity_type='Cycling', duration=45, date='2025-04-19').save()

        # Create test leaderboard entries
        Leaderboard(user=user1, score=100).save()
        Leaderboard(user=user2, score=80).save()

        # Create test workouts
        Workout(name='Morning Yoga', description='A relaxing yoga session', duration=60).save()
        Workout(name='HIIT', description='High-intensity interval training', duration=30).save()

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data'))
