from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    username = models.CharField(max_length=150, unique=True, blank=False)
    email = models.CharField(max_length=200, unique=True, blank=False)

    def __str__(self):
        return self.username + ': ' + self.email


class Relationship(models.Model):
    user = models.ForeignKey(Profile, max_length=150, blank=False, related_name='friends',
                             on_delete=models.CASCADE)
    friend = models.ForeignKey(Profile, max_length=150, blank=False, related_name='requests_from',
                               on_delete=models.CASCADE)
    is_pending = models.BooleanField(default=True)

    def __str__(self):
        return 'user: %s, friend: %s, isPending: %s' % (self.user.username, self.friend.username, self.is_pending)

    class Meta:
        unique_together = ('user', 'friend')
