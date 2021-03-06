from django.db import models


class GameUser(models.Model):
    access_token = models.CharField(max_length=255)
    real_access_token = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(blank=True)
    room = models.CharField(max_length=255, null=True, blank=True)


class Game(models.Model):
    user1 = models.ForeignKey(GameUser, related_name='user1_rel')
    user2 = models.ForeignKey(GameUser, related_name='user2_rel', blank=True, null=True)
    user1_points = models.IntegerField(null=True, blank=True)
    user2_points = models.IntegerField(null=True, blank=True)
    board = models.TextField(null=True, blank=True)
    board_solved = models.TextField(null=True, blank=True)
    datetime = models.DateTimeField(auto_now_add=True, null=True, blank=True)
