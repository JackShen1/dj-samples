from django.db import models
from django.core.validators import MinLengthValidator
from django.conf import settings


class Pic(models.Model):
    title = models.CharField(
        max_length=200,
        validators=[MinLengthValidator(2, 'Title must be greater than 2 characters')]
    )
    text = models.TextField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    picture = models.BinaryField(null=True, blank=True, editable=True)
    content_type = models.CharField(max_length=256, null=True, blank=True,
                                    help_text='The MIMEType of the field')
    # That's really important when you're uploading the file, you get them have it, and then you have to send it back
    # out. Otherwise, the browser will not know how to properly format this. So that is what is here. That's the
    # content-type. It's just a string field. The content-type is just a string, but it's very important to track it.
    # So when I am on Add, when I upload the file, and I pick it, it's actually communicated to me as part of the
    # uploaded data. But I got to remember, I got our actual pixels go in here, and the content-type goes in its own
    # character field. The pixels of the picture, the actual colors, and stuff go into this binary field. I'm going to
    # use the owner. So we're going to have this, we did this before, we have an owner, and that's just going to be
    # automatically created when there's owners.py.

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Shows up in admin list
    def __str__(self):
        return self.title
