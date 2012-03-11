from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url( r'^app/$', 'app.views.index' ),
                       url( r'^app/submit$', 'app.views.submit' ),
                       url( r'^app/help$', 'app.views.help' ),
                       url( r'^app/about$', 'app.views.about' ),
                       url( r'^app/contact$', 'app.views.contact' ),
                       url( r'^app/alltime$', 'app.views.allTime' ),
                       url( r'^app/week$', 'app.views.week' ),
                       url( r'^app/month$', 'app.views.month' ),
                       url( r'^app/search$', 'app.views.search' ),
                       url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
                       url(r'^admin/', include(admin.site.urls)),
)
