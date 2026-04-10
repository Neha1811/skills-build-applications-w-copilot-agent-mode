
from rest_framework import generics
from .models import User, Team, Activity, Workout, Leaderboard
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, WorkoutSerializer, LeaderboardSerializer

class UserListView(generics.ListCreateAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class TeamListView(generics.ListCreateAPIView):
	queryset = Team.objects.all()
	serializer_class = TeamSerializer

class ActivityListView(generics.ListCreateAPIView):
	queryset = Activity.objects.all()
	serializer_class = ActivitySerializer

class WorkoutListView(generics.ListCreateAPIView):
	queryset = Workout.objects.all()
	serializer_class = WorkoutSerializer

class LeaderboardListView(generics.ListCreateAPIView):
	queryset = Leaderboard.objects.all()
	serializer_class = LeaderboardSerializer
