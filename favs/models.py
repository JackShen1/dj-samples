from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User
from django.conf import settings

class Thing(models.Model) :
    title = models.CharField(
            max_length=200,
            validators=[MinLengthValidator(2, "Title must be greater than 2 characters")]
    )
    text = models.TextField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
            related_name='fav_thing_owner')
    favorites = models.ManyToManyField(settings.AUTH_USER_MODEL,
        through='Fav', related_name='favorite_things')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Shows up in the admin list
    def __str__(self):
        return self.title

class Fav(models.Model) :

    thing = models.ForeignKey(Thing, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name='favs_users')

    # https://docs.djangoproject.com/en/3.0/ref/models/options/#unique-together
    # That simply means that you can't insert more than one combination of a thing and a user. So it's not like you can
    # fav it a lot. If you keep hitting favorite, there's only one row. If there's a row in here that exists, ie right
    # here, if this row exists and it connects the two, then it's favorite.
    class Meta:
        unique_together = ('thing', 'user')

    def __str__(self) :
        return '%s likes %s'%(self.user.username, self.thing.title[:10])
