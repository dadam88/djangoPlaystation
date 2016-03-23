from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'playstation.views.home_page', name='home_page'),
    url(r'^game_details/(?P<gameslug>.*)/$', 'playstation.views.game_details', name='game_details'),
    url(r'^admin/', include(admin.site.urls)),
]