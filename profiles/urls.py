from django.urls import path
from . import views


urlpatterns = [
    path('u/<slug:slug>/', views.PublicProfileView.as_view(), name='public_profile'),
    path('link/<int:link_id>/click/', views.increment_link_click, name='increment_link_click'),
]
