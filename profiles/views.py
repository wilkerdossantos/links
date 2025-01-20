from django.views.generic import DetailView
from .models import Link, Brand, PageView
from django.shortcuts import get_object_or_404, redirect


class PublicProfileView(DetailView):
    model = Brand
    template_name = 'public_profile.html'
    context_object_name = 'brand'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['links'] = Link.objects.filter(brand=self.object)
        return context

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)

        # Obtém o IP com fallbacks
        x_forwarded_for = self.request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip_address = x_forwarded_for.split(',')[0]
        else:
            ip_address = self.request.META.get('REMOTE_ADDR', '0.0.0.0')

        brand = self.object
        PageView.objects.create(brand=brand, ip_address=ip_address)
        brand.total_visualizacoes += 1
        brand.save()

        return response
    
class BioView(DetailView):
    model = Brand
    template_name = 'bio.html'
    context_object_name = 'brand'


def track_click(request, link_id):
    link = get_object_or_404(Link, id=link_id)
    link.clicks_count += 1
    link.save()
    return redirect(link.url)
