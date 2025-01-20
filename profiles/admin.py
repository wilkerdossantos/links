from django.contrib import admin
from .models import Link, Brand


admin.site.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'order')


admin.site.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('nome_marca', 'email', 'descricao', 'tema', 'slug')
    prepopulated_fields = {'slug': ('nome_marca',)}
