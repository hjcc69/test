from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views
admin.autodiscover()
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('blog.url')),
    url(r'^accounts/login/$', views.login, name='login'),
    url(r'^accounts/logout/$', views.logout, name='logout', kwargs={'next_page': '/'}),
    # Uncomment the admin/doc line below to enable admin documentation:

   # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:

]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)