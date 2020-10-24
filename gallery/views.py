from django.shortcuts import render
from .models import Image
from .forms import ImageForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
import os

# Create your views here.
@login_required
def galleryView(request):
    data = {}
    data['imgs'] = Image.objects.all().filter(user=request.user)
    return render(request, 'gallery/gallery.html', data)

@login_required
def removeAllImages(request):
    Images = Image.objects.all().filter(user=request.user)
    for img in Images:
        os.remove(img.image.path)
    Images.delete()
    return redirect('/gallery')

@login_required
def addImage(request):
    data = {}
    if request.method == 'POST':
        data['form'] = ImageForm(request.POST, request.FILES)

        if data['form'].is_valid():
            image = Image()
            image.title = data['form'].cleaned_data['title']
            image.image = data['form'].cleaned_data['image']
            image.user = request.user
            image.save()
            # messages.success(request, "'" + task.__str__() + "'" + " Task added!")
            return redirect('/gallery')
    else:
        data['form'] = ImageForm()
        return render(request, 'gallery/addImage.html', data)

@login_required
def removeImage(request, id):
    img = get_object_or_404(Image, pk=id)
    os.remove(img.image.path)
    img.delete()
    return redirect('/gallery')

@login_required
def viewImage(request, id):
    data = {}
    data['img'] = get_object_or_404(Image, pk=id)
    return render(request, 'gallery/viewImage.html', data)