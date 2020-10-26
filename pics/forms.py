from django import forms
from pics.models import Pic
from django.core.files.uploadedfile import InMemoryUploadedFile
from pics.humanize import naturalsize


# Create the form class.
class CreateForm(forms.ModelForm):
    max_upload_limit = 2 * 1024 * 1024
    max_upload_limit_text = naturalsize(max_upload_limit)

    # Call this 'picture' so it gets copied from the form to the in-memory model
    # It will not be the "bytes", it will be the "InMemoryUploadedFile"
    # because we need to pull out things like content_type
    picture = forms.FileField(required=False, label='File to Upload <= ' + max_upload_limit_text)
    upload_field_name = 'picture'

    # Hint: this will need to be changed for use in the ads application :)
    class Meta:
        model = Pic
        fields = ['title', 'text', 'picture']  # Picture is manual

    # So clean is one of the life cycles of a model form. Meaning once the data comes in, it's going to ask to be
    # cleaned. So what we do is we call it super class, the model form class, and do the clean there. It doesn't know
    # anything about picture because we're the one that added that. But then we get the data in cleaned data, and it's a
    # dictionary at that point, and so I can get the picture. So remember that the form is the part that's coming in
    # from the browser, and then I can make the picture, I can get it from there. If I got no pictures, I don't need to
    # do anything special. If I do, I'm checking to see if the amount of data that I got from that upload is greater
    # than that upload limit, it's good. So this is mostly here to check to make sure I'm cleaning the data, I'm not
    # actually saving it, but I'm grabbing the picture from the form, and I'm checking to see if it's greater than two
    # megabytes and then I'm going to add, this is what you do in clean. Clean is just to say a nasty message.

    # Validate the size of the picture
    def clean(self):
        cleaned_data = super().clean()
        pic = cleaned_data.get('picture')
        if pic is None: return
        if len(pic) > self.max_upload_limit:
            self.add_error('picture', "File must be < " + self.max_upload_limit_text + " bytes")

    # Convert uploaded File object to a picture
    def save(self, commit=True):
        instance = super(CreateForm, self).save(commit=False)

        # We only need to adjust picture if it is a freshly uploaded file
        f = instance.picture  # Make a copy
        if isinstance(f, InMemoryUploadedFile):  # Extract data from the form to the model
            bytearr = f.read()
            instance.content_type = f.content_type
            instance.picture = bytearr  # Overwrite with the actual image data

        if commit:
            instance.save()

        return instance

# https://docs.djangoproject.com/en/3.0/topics/http/file-uploads/
# https://stackoverflow.com/questions/2472422/django-file-upload-size-limit
# https://stackoverflow.com/questions/32007311/how-to-change-data-in-django-modelform
# https://docs.djangoproject.com/en/3.0/ref/forms/validation/#cleaning-and-validating-fields-that-depend-on-each-other
