from django.forms import ModelForm
from autos.models import Make


#  So the form file is interesting, because we've seen forms that are just forms by themselves, but this is a special
#  kind of form and then it's a ModelForm. In that, we normally in the other models, we had all these fields, and we put
#  them in and it looked a lot like a model file where we have a character field, PositiveIntegerField. But what we're
#  basically saying is, you know what? We're going to make a form here. Really, all we want to do is take all the fields
#  from the Make model and make them form fields. So a form and a model are two different things. A form is something
#  that goes between the view and the template, and as you'll see, it also goes down into the models automatically,
#  so this is just like make all the fields. Let's make a form because form objects don't have to be associated with
#  models. But in this case, we're going to derive a form object from a model. So instead of extending form, we're
#  extending ModelForm. So that's a ModelForm must have, and this is just some data that says the model that we're
#  going to pull all our fields from is the Make model, and it only has one thing which is a name. That's it. So this
#  is auto generating a form that if we changed it and added another field here, then this make form would automatically
#  have a field. You can give it a list of fields, _ _ all _ _ is like a signal to say," Just give me all of them."
#  Now there might be some internal things like created at and updated at or something that you don't want to use.
#  So that's a form, remember how forms work. We cover that before.

# Create the form class.
class MakeForm(ModelForm):
    class Meta:
        model = Make
        fields = '__all__'

