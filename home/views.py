
from django.shortcuts import render,redirect
from .forms import RegistrationForm
from django.http import HttpResponseRedirect
# Create your views here.
def index(request):
    return render(request, 'pages/bandtemplate.html')
def contact(request):
    return render(request, 'pages/contact.html')
def error(request):
    return render(request, 'pages/error.html')
def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'pages/register.html', {'form': form})
def error(request, *args, **kwargs):
    return redirect('https://your-site/404')
