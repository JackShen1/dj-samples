from django.db import models
from django.conf import settings


# Create your models here.
# So there is a data model for this, it's a one-to-many, we've got text fields, we got a primary key, everybody can put
# more fields in so that we do know who they're owned by, so that we know who is allowed. We do have an owner, but we
# don't have any trashing. So we don't have to delete this, is a really quite simple at this point. So we got the two
# fields created at and updated up, of course are handled automatically.
class Message(models.Model) :
    text = models.TextField();
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
