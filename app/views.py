from app.models import Incident
from django.http import HttpResponse
from django.shortcuts import render_to_response

def index( request ):
    incidents = sorted( Incident.objects.all(), key = lambda i: i.netVote(), reverse=True )
    incidents = filter( lambda i: i.was_submitted_today(), incidents )
    return render_to_response( 'app/index.html', { 'incidents': incidents } )

def week( request ):
    incidents = sorted( Incident.objects.all(), key = lambda i: i.netVote(), reverse=True )
    incidents = filter( lambda i: i.was_submitted_past_week(), incidents )
    return render_to_response( 'app/index.html', { 'incidents': incidents } )

def month( request ):
    incidents = sorted( Incident.objects.all(), key = lambda i: i.netVote(), reverse=True )
    incidents = filter( lambda i: i.was_submitted_past_month(), incidents )
    return render_to_response( 'app/index.html', { 'incidents': incidents } )

def allTime( request ):
    incidents = sorted( Incident.objects.all(), key = lambda i: i.netVote(), reverse=True )
    return render_to_response( 'app/index.html', { 'incidents': incidents } )

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
