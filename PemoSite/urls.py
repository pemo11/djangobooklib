"""PemoSite URL Configuration

"""
from django.contrib import admin
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalog/', include('catalog.urls')),
    path('', RedirectView.as_view(url='/catalog/'))
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)