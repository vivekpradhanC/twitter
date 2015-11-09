from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tweets(models.Model):
    text=models.TextField(' tweets ' , max_length = 150 , db_index = True )
    author=models.ForeignKey (User, verbose_name = ' author ')
    created=models.DateTimeField(' creation time ' , auto_now_add = True )

    class Meta:
        ordering = ['-created']
    def __str__(self):
        return self.text


class Tweeter(models.Model):
    user=models.ForeignKey(User, verbose_name='author', related_name='user_for_follower_and_following')
    folowers=models.ManyToManyField(User, verbose_name='folowers', related_name='user_followers')
    following=models.ManyToManyField(User, verbose_name='folowing', related_name='user_following')



