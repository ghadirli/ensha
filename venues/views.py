from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Venue
from django.shortcuts import render, redirect, get_object_or_404


@login_required
def create_venue(request):
    if request.method == 'POST':
        # Get the form data from the request
        name = request.POST.get('name')
        description = request.POST.get('description')
        # Create a new venue object
        venue = Venue.objects.create(name=name, description=description)
        # Redirect to the venue list page or any other appropriate page
        return redirect('venue_list')
        # Redirect to the venue list page or any other page you want
    else:
        return render(request, 'create_venue.html')


def venue_list(request):
    venues = Venue.objects.all()
    return render(request, 'venue_list.html', {'venues': venues})


def venue_detail(request, venue_id):
    venue = get_object_or_404(Venue, pk=venue_id)
    articles = venue.articles.all()
    return render(request, 'venue_detail.html', {'venue': venue, 'articles': articles})

# Create your views here.
