import os
from .forms import ImageForm
from django.shortcuts import render
from django.conf import settings

from PIL import Image
from imageclassifierapp.services.classifier import Classifier

def main(request):
    form = ImageForm(request.POST, request.FILES)
    if request.method == "POST":

        if form.is_valid():
            form.save()

    path  = os.path.join(settings.BASE_DIR, 'images/airplane.jpg')
    image = Image.open(path)

    prediction = Classifier(image).classify()
    
    return render(request, 'imageclassifierapp/index.html', { 'prediction' : prediction,'form':form })

