from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User
from django.conf import settings


class Article(models.Model):
    title = models.CharField(
        max_length=200,
        validators=[MinLengthValidator(2, 'Title must be greater than 2 characters')]
    )
    text = models.TextField()
    # So it's just another field, it turns out to be an integer. It's a foreign key, like all integers. All foreign keys
    # are integers. On delete models cascade, you have seen that before. That's simply means if we have a bunch of
    # articles that are linked to a user and we delete that user, it deletes the four articles that were associated with
    # the user in order to keep the internal pointers consistent. So that part is all the same, quite comfortable and
    # you've been doing that for a while. Now, settings of user model. We're importing settings from Django, and we are
    # making a foreign key to a model that is not ours. It is something that Django maintains, so Django always has a
    # user model somewhere. It may be named one thing or a different thing, we just don't know. We don't know what the
    # name of the user model is, and so we have to ask Django for it, and Django conveniently always leaves it in this
    # location. settings.AUTH_USER_MODEL. It turns out if you want to change it, you got to change that variable.
    # But for us, we're not going to change where it's at, Django is going to set it for us and we're just going to use
    # it. So there's two tables. There's this article table and some user table somewhere, and there's a foreign key
    # relationship between them in a database level. Once you make this database, you could go see what the name of that
    # table is because it will show you the create statement that it actually used, not that that matters. So it's
    # pretty much a normal thing like we've been making, except it's got this extra owner column. That's the thing we're
    # focusing on right now.
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Shows up in the admin list
    def __str__(self):
        return self.title
