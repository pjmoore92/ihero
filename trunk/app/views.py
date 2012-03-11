from app.models import Incident
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.db.models import Q
from django.core.mail import send_mail
from forms import ContactForm
import datetime


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

def addVote( request, incident_id ):
    incident = Incident.objects.get( pk = incident_id )
    downvote = request.GET.get( 'down', '' )
    incident.decVote() if downvote else incident.incVote()
    incident.save()
    return render_to_response( 'app/index.html' )

def submit( request ):
    return render_to_response( 'app/submit.html' )

def about( request ):
    return render_to_response( 'app/about.html' )

def help( request ):
    return render_to_response( 'app/help.html' )

def addIncident( request ):
    title = request.GET.get( 'title', '' )
    description = request.GET.get( 'description', '' )

    if title and description:
        incident = Incident( title = title, description = description,
                             submission_time = datetime.date.today(), upvotes = 0, downvotes = 0 )
        incident.save()
    else:
        return render_to_response( 'app/index.html' )
    return render_to_response( 'app/addIncident.html' );

def hit(request, incident_ik):
    Incident.objects.filter(ik=incident_ik).update(upvotes=F('upvotes')+1)
    return HttpResponse()

def search( request ):
    query = request.GET.get( 'q', '' )
    if query:
        qset = ( Q( title__icontains = query ) |
                 Q( description__icontains = query ) )
        results = Incident.objects.filter( qset ).distinct()
    else:
        results = []
    return render_to_response( "app/index.html", { "incidents" : results } )

def contact( request ):
    if request.method == 'POST':
        form = ContactForm( request.POST )
        if form.is_valid():
            fdata = form.cleaned_data
            send_mail( fdata[ 'topic' ], fdata[ 'message' ], 
                       fdata[ 'sender' ], [ 'gareeblackwood@gmail.com' ] )
            return render_to_response( 'app/thanks.html' )
    else:
        form = ContactForm()
    return render_to_response( 'app/contact.html', { "form" : form } )
