
from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
	def setUp(self):
		self.team = Team.objects.create(name="Team A")
		self.user = User.objects.create(name="User1", email="user1@example.com", team=self.team)

	def test_create_activity(self):
		activity = Activity.objects.create(user=self.user, type="Run", duration=30)
		self.assertEqual(activity.type, "Run")

	def test_create_workout(self):
		workout = Workout.objects.create(user=self.user, description="Pushups", duration=10)
		self.assertEqual(workout.description, "Pushups")

	def test_leaderboard(self):
		lb = Leaderboard.objects.create(user=self.user, points=100)
		self.assertEqual(lb.points, 100)
