from django.conf import settings
from django.conf.urls import include,url
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    url(r'^app1/', include('app1.urls')),
    url(r'^admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
]



if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
