from django.forms import ModelForm
from photo.models import Photography


class PhotoForm(ModelForm):
    class Meta:
        model = Photography
        fields = ['photo']