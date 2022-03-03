import os

from django.shortcuts import render
from django.conf import settings

from PIL import Image

from .forms import ImageForm
from .services.classifier import Classifier

from .models import ImgClass


def main(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)

        if form.is_valid():
            image = Image.open(form.cleaned_data.get('image'))
            prediction = Classifier(image).classify()
            image_name = form.cleaned_data.get('image').name
            image_path = os.path.abspath(image_name)
            ImgClass.objects.create(img_path=image_path, img_classifier=prediction)
            return render(request, 'imageclassifierapp/index.html', { 'prediction' : prediction, 'form' : form })
    
    form = ImageForm()
    Images = ImgClass.objects.all()
    return render(request, 'imageclassifierapp/index.html', context={'form' : form, 'Images': Images })

