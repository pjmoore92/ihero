from app.models import Incident
from django.http import HttpResponse
from django.shortcuts import render_to_response

def index( request ):
    latest_incidents = Incident.objects.all()
    latest_incidents = sorted( latest_incidents, key = lambda i: i.netVote(), reverse=True )
    return render_to_response( 'app/index.html', { 'latest_incidents': latest_incidents } )

def submit( request ):
    return render_to_response( 'app/submit.html' )

def about( request ):
    return render_to_response( 'app/about.html' )

def help( request ):
    return render_to_response( 'app/help.html' )

def contact( request ):
    return render_to_response( 'app/contact.html' )

def hit(request, incident_ik):
    Incident.objects.filter(ik=incident_ik).update(upvotes=F('upvotes')+1)
    return HttpResponse()
