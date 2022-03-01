import os

from django.shortcuts import render
from django.conf import settings
from .forms import ImageForm
from .models import Image

from PIL import Image
from imageclassifierapp.services.classifier import Classifier

def main(request):
    path  = os.path.join(settings.BASE_DIR, 'images/airplane.jpg')
    image = Image.open(path)

    prediction = Classifier(image).classify()
    
    return render(request, 'imageclassifierapp/index.html', { 'prediction' : prediction })

def index(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    form = ImageForm()
    img = Image.objects.all()
    return render(request, 'imageclassifierapp/index.html', {'img':img, 'form':form})
