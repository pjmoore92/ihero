from django.db import models

class Incident( models.Model ):
    title = models.CharField( max_length = 200 )
    description = models.TextField()
    submission_time = models.DateTimeField( 'Submission Time' )
    upvotes = models.PositiveIntegerField()
    downvotes = models.PositiveIntegerField()

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

    

    
