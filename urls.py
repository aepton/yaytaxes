from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

#(r'', 'main.views.index'),
urlpatterns = patterns('',
	(r'^main$', 'main.views.index'),
	(r'^main/$', 'main.views.index'),
	(r'^main/tweets$', 'main.views.tweets'),
	(r'^main/metrics$', 'main.views.metrics'),
	(r'^main/incomes$', 'main.views.incomes'),
	(r'^main/yaytaxesland$', 'main.views.yaytaxesland'),
	
    # Example:
    # (r'^yaytaxes/', include('yaytaxes.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
