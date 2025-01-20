from django.contrib import admin
from .models import Link, Brand


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'order', 'clicks_count',)
    readonly_fields = ('clicks_count',)


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('nome_marca', 'slug', 'total_visualizacoes',)
    prepopulated_fields = {'slug': ('nome_marca',)}
    readonly_fields = ('total_visualizacoes',)
