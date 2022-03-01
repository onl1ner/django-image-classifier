import os

from django.shortcuts import render
from django.conf import settings

from PIL import Image

from .forms import ImageForm
from .services.classifier import Classifier

def main(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
    
        if form.is_valid():
            image = Image.open(form.cleaned_data.get('image'))
            prediction = Classifier(image).classify()
            
            return render(request, 'imageclassifierapp/index.html', { 'prediction' : prediction, 'form' : form })
    
    form = ImageForm()
    return render(request, 'imageclassifierapp/index.html', { 'form' : form })

