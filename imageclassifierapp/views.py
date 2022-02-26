import os

from django.shortcuts import render
from django.conf import settings

from PIL import Image
from imageclassifierapp.services.classifier import Classifier

def main(request):
    path  = os.path.join(settings.BASE_DIR, 'images/airplane.jpg')
    image = Image.open(path)

    prediction = Classifier(image).classify()
    
    return render(request, 'imageclassifierapp/index.html', { 'prediction' : prediction })