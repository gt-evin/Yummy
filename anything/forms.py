from django import forms

from anything.models import ImageModel


class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageModel
        fields = ['image','title','price']