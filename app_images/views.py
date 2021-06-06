from django.shortcuts import render

# Create your views here.
def images(request):
    return render(request ,'app_images/images_uncle.html')
