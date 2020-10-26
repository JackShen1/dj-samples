from django.db import models
from django.core.validators import MinLengthValidator


# We're going to make a Make object class. It's going to have one character field with some validators in it.
# We play with that with forms. You can put validators in models. We've previously seen validators in form, but there's
# a validator that basically says, we're not going to accept data coming into this database table unless there's at
# least two characters. This _str_, you've been doing this for awhile. That basically is if you take a model object
# an actual make and you print it, it says which of the fields, in this case, there's only one field. So that just says
# when we're converting a model object to a string, we get to decide how that looks.
class Make(models.Model):
    name = models.CharField(
            max_length=200, 
            help_text='Enter a make (e.g. Dodge)',
            validators=[MinLengthValidator(2, "Make must be greater than 1 character")]
    )

    def __str__(self):
        """String for representing the Model object."""
        return self.name


# Then we have an automobile and it's got a nickname with a MinLengthValidator, max_length of 200, and mileage, which
# has an integer field, a comments, which is a 300 character field, and then a foreign key in too. This as a one-to-many
# or many-to-one relationship, not a many-to-many, just a foreign key into to Make. Then we're going to on_delete
# CASCADE which really means if you delete a Make, then the corresponding auto entries will automatically be deleted.
# So this is a pretty straightforward model, actually very, very simple.
# Once again, we're always defining this _str_(self) so that we know that if you're just showing it like in the admin
# interface or if you're just printing it or just converting the model itself to a string, the field among these fields
# that is supposed to be used is the nickname field, just to show to end-users.
class Auto(models.Model) : 
    nickname = models.CharField(
            max_length=200,
            validators=[MinLengthValidator(2, "Nickname must be greater than 1 character")]
    )
    mileage = models.PositiveIntegerField()
    comments = models.CharField(max_length=300)
    make = models.ForeignKey('Make', on_delete=models.CASCADE, null=False)

    # Shows up in the admin list
    def __str__(self):
        return self.nickname
