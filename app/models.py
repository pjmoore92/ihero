import calendar
import datetime
from datetime import timedelta
from django.db import models

class Incident( models.Model ):
    title = models.CharField( max_length = 200 )
    description = models.TextField()
    submission_time = models.DateTimeField( 'Submission Time' )
    upvotes = models.PositiveIntegerField()
    downvotes = models.PositiveIntegerField()
    location = models.TextField()
    category = models.TextField()

    def __unicode__( self ):
        return self.title

    def incVote( self ):
        self.upvotes += 1

    def decVote( self ):
        self.downvotes += 1

    def netVote( self ):
        return self.upvotes - self.downvotes

    def was_submitted_today( self ):
        return self.submission_time.date() == datetime.date.today()

    def was_submitted_past_week( self ):
        delta = timedelta( days = 7 )
        week_ago = datetime.date.today() - delta
        return self.submission_time.date() >= week_ago

    def was_submitted_past_month( self ):
        days_in_month = calendar.mdays[ datetime.date.today().month ]
        delta = timedelta( days = days_in_month )
        month_ago = datetime.date.today() - delta
        return self.submission_time.date() >= month_ago




