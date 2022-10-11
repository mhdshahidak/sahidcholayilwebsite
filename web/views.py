from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Award, Gallery, Position, Update
from .forms import ContactForm
import json


def index(request):
    updates = Update.objects.filter().order_by('-id')[:6]
    gallery = Gallery.objects.filter().order_by('-id')[:8]
    context = {
        'updates': updates,
        'gallery': gallery
    }
    return render(request, 'web/index.html', context)


def about(request):
    return render(request, 'web/about.html')


def updates(request):
    updates = Update.objects.all()
    context = {
        'updates': updates
    }
    return render(request, 'web/updates.html', context)


def gallery(request):
    gallery = Gallery.objects.all()
    context = {
        'gallery': gallery
    }
    return render(request, 'web/gallery.html', context)


def position(request):
    position = Position.objects.all()
    context = {
        'position': position
    }
    return render(request, 'web/position.html', context)


def awards(request):
    award = Award.objects.all()
    context = {
        'award': award
    }
    return render(request, 'web/awards.html', context)


def contact(request):
    contact = ContactForm(request.POST or None)
    if request.method == 'POST':
        if contact.is_valid():
            data = contact.save(commit=False)
            data.save()
            response_data = {
                "status": "true",
                "title": "Submited",
                "message": "Thank you for getting in touch!"
            }
        else:
            print(contact.errors)
            response_data = {
                "status": "false",
                "title": "Form validation error",
            }
        return HttpResponse(json.dumps(response_data), content_type='application/javascript')
    context = {
        'contact': contact,
    }
    return render(request, 'web/contact.html', context)
