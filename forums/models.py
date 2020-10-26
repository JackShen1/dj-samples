from django.db import models
from django.core.validators import MinLengthValidator
from django.conf import settings


# So owner is a one-to-many relationship. That is that, there is a user table, and then there is a forum table, and each
# user can have many forums. So each user can have many forums. So that is our table. Now, what's going to happen is,
# the interesting part is here, but let's first talk about the comment table. So the comment table is down here. The
# comment table has one user can have many comments and one forum can have many comments as well. Because there is a
# many-to-many relationship between users in forums with a little bit of comment data sitting right there in the middle,
# that has to be modeled as a completely separate table. There's only two tables here but really there's three tables
# here because the user table is participating in both of these models. We'll come back to the many-to-many field. This
# is the comment, and like connection tables or junction tables are joined tables, it has two ForeignKeys. It's the most
# important thing. It's the keys in each direction, I guess I shouldn't change that. We got the user table, we got the
# comment table, and we got the forum table. Forums can have many comments. Users can have many comments. These are
# forum and so a user can have many forums. This side of it is a ForeignKey, and this is a ForeignKey as well. Coming
# out of the common table, there are two ForeignKeys and look at that. There is a form key aimed at the forum model and
# then a ForeignKey coming out of the comment to the user model. Now again, in the lectures, we've talked about modeling
# data at the connection so the text that we're getting at the modeling point is this text right here. It is the actual
# comment itself. You could make a different table for it, but it's just as easy to model it right in the middle of the
# junction field, that's pretty much it.
class Forum(models.Model):
    title = models.CharField(
        max_length=200,
        validators=[MinLengthValidator(5, "Title must be greater than 5 characters")]
    )
    text = models.TextField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='forums_owned')
    # In a sense, what we're seeing here is this basically says that there is a relationship between forums and users,
    # and it is in the comments table. The table that it goes through is the comments table. That's what the through
    # means. Then the related name equals forum comments is actually you're installing in the user object, a method and
    # attribute, something in this user model that says forum comments so we're actually extending the user model. If
    # we're looking at the user, we could say, "Hey, what are the forum comments for this user?" We'd come over here and
    # it would give us a list of all the forums. Actually, no, no, sorry. It would come over here and give us a list of
    # all the comments. But this related name is the name of this attribute. You don't necessarily need all the time to
    # be able to do this. But the problem is after a while when you're plugging so many things into the user model, you
    # can end up with name conflicts and so it's good to name this thing even though we might not use it. I hope that
    # helps. This is a pretty straightforward thing other than the fact that the user model is our third table and we're
    # using it in both places so there is that.
    comments = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Comment', related_name='forum_comments')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Shows up in the admin list
    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.TextField(
        validators=[MinLengthValidator(3, "Comment must be greater than 3 characters")]
    )

    forum = models.ForeignKey(Forum, on_delete=models.CASCADE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Shows up in the admin list
    def __str__(self):
        if len(self.text) < 15: return self.text
        return self.text[:11] + ' ...'
