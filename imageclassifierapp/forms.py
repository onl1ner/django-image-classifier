from django import forms
from .models import ImgClass


class ImageForm(forms.Form):
    image = forms.ImageField()

    class Meta:
        model = ImgClass
        fields = {'img_path', 'img_classifier', 'photo'}
