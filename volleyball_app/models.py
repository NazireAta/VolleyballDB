from django.db import models

class DatabaseManager(models.Model):
    username = models.CharField(max_length=512, primary_key=True)
    password = models.CharField(max_length=512)

class Player(models.Model):
    username = models.CharField(max_length=512, primary_key=True)
    password = models.CharField(max_length=512)
    name = models.CharField(max_length=512)
    surname = models.CharField(max_length=512)
    date_of_birth = models.CharField(max_length=512)
    height = models.IntegerField()
    weight = models.IntegerField()

class Coach(models.Model):
    username = models.CharField(max_length=512, primary_key=True)
    password = models.CharField(max_length=512)
    name = models.CharField(max_length=512)
    surname = models.CharField(max_length=512)
    nationality = models.CharField(max_length=512)

class Jury(models.Model):
    username = models.CharField(max_length=512, primary_key=True)
    password = models.CharField(max_length=512)
    name = models.CharField(max_length=512)
    surname = models.CharField(max_length=512)
    nationality = models.CharField(max_length=512)

class Positions(models.Model):
    position_id = models.IntegerField(primary_key=True)
    position_name = models.CharField(max_length=512)

class Team(models.Model):
    team_id = models.IntegerField(primary_key=True)
    team_name = models.CharField(max_length=512)
    coach_username = models.CharField(max_length=512)
    contract_start = models.CharField(max_length=512)
    contract_finish = models.CharField(max_length=512)
    channel_id = models.IntegerField()

class CoachTeam(models.Model):
    team_id = models.IntegerField()
    coach_id = models.CharField(max_length=20)
    contract_start = models.DateField()
    contract_finish = models.DateField()

class TVChannel(models.Model):
    channel_id = models.IntegerField(primary_key=True)
    channel_name = models.CharField(max_length=512)

class Stadium(models.Model):
    stadium_id = models.IntegerField(primary_key=True)
    stadium_country = models.CharField(max_length=512)
    stadium_name = models.CharField(max_length=512)

class PlayerPositions(models.Model):
    player_positions_id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=512)
    position = models.IntegerField()

class PlayerTeams(models.Model):
    player_teams_id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=512)
    team = models.IntegerField()

class SessionSquads(models.Model):
    squad_id = models.IntegerField(primary_key=True)
    session_id = models.IntegerField()
    played_player_username = models.CharField(max_length=512)
    position_id = models.IntegerField()

class MatchSession(models.Model):
    session_id = models.IntegerField(primary_key=True)
    team_id = models.IntegerField()
    stadium_id = models.IntegerField()
    time_slot = models.IntegerField()
    date = models.CharField(max_length=512)
    assigned_jury_username = models.CharField(max_length=512)
    rating = models.FloatField()