from django.forms import ModelForm
from cats.models import Breed


class BreedForm(ModelForm):
    class Meta:
        model = Breed
        fields = '__all__'
