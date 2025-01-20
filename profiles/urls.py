from django.urls import path
from . import views


urlpatterns = [
    path('<slug:slug>/', views.PublicProfileView.as_view(), name='public_profile'),
    path('click/<int:link_id>/', views.track_click, name='track_click'),
    path('bio/<slug:slug>/', views.BioView.as_view(), name='bio'),
]
