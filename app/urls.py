from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect


def redirect_to_profile(request):
    return redirect('public_profile', slug='mandapamonha')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', redirect_to_profile, name='redirect_to_profile'), 
    path('', include('profiles.urls')),
    path('', include('accounts.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
