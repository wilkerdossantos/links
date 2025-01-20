from django.views.generic import DetailView
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Link, Brand, PageView


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

@require_POST
def increment_link_click(request, link_id):
    try:
        link = Link.objects.get(id=link_id)
        link.clicks_count += 1
        link.save()
        return JsonResponse({'success': True, 'clicks': link.clicks_count})
    except Link.DoesNotExist:
        return JsonResponse({'success': False}, status=404)
