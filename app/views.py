from app.models import Incident
from django.http import HttpResponse
from django.template import Context, loader


def index( request ):
    latest_incidents = Incident.objects.all()
    t = loader.get_template( 'app/index.html' )
    c = Context( { 'latest_incidents': latest_incidents, } )
    return HttpResponse( t.render( c ) )

def submit( request ):
    return HttpResponse( "Submit view" )

def incident( request, incident_id ):
    return HttpResponse( "You are looking at the incident %s" % incident_id )

def about( request ):
    return HttpResponse( "About us" )

def help( request ):
    return HttpResponse( "Help page" )


