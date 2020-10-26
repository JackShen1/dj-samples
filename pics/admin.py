from django.contrib import admin
from pics.models import Pic


# We want the admin UI to leave the picture and content_type alone
# So if I'm to take a look at the pics, so it turned out that I didn't want either of these two things to show up
# because it turned out it made it difficult because I couldn't update things. So you won't see picture or content_type
# here in admin, and I do that by excluding this. Instead of doing a shortcut, I'm going to register for the model Pic
# this particular class. It allows me to have this class-wide variable called exclude so that I don't show those things.
# Define the PicAdmin class
class PicAdmin(admin.ModelAdmin):
    exclude = ('picture', 'content_type')


# Register the admin class with the associated model
admin.site.register(Pic, PicAdmin)
