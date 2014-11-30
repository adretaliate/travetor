from django.conf.urls import patterns, include, url
from django.contrib import admin
from welcome import views
admin.autodiscover()


urlpatterns = patterns('',
		url(r'^$','welcome.views.home',name='home'),
		url(r'^restricted/', include(admin.site.urls)),
		url(r'^blog/$','details.views.show_blog',name='blog'),
		url(r'^about-us/$','welcome.views.aboutus',name='aboutus'),
		url(r'^contact-us/$','welcome.views.contactus',name='contactus'),
		url(r'^FAQ/$','welcome.views.faq',name='faq'),
		url(r'^special-packages/$','welcome.views.specialpackages',name='special'),
		url(r'^(?P<cat_slug>[-\w]+)/$','details.views.show_category',name='showcategory'),
		url(r'^(?P<cat_slug>[-\w]+)/(?P<tr_slug>[-\w]+)/$','details.views.show_trek',name='showtrek'),
    # Examples:
    # url(r'^$', 'travetor.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    	
)