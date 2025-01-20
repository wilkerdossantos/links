from django.db import models
from django.utils.text import slugify
from accounts.models import User


class Brand(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="brand")
    nome_marca = models.CharField(max_length=255, default="Minha Marca")
    descricao = models.TextField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    logotipo = models.ImageField(upload_to="logotipos/", blank=True, null=True)
    tema = models.CharField(max_length=50, default="padrao")
    slug = models.SlugField(unique=True, blank=True, null=True)
    total_visualizacoes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nome_marca

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nome_marca)
        super().save(*args, **kwargs)


class Link(models.Model):
    URL_CHOICES = [
        ("facebook", "Facebook"),
        ("instagram", "Instagram"),
        ("linkedin", "LinkedIn"),
        ("pinterest", "Pinterest"),
        ("reddit", "Reddit"),
        ("snapchat", "Snapchat"),
        ("spotify", "Spotify"),
        ("tiktok", "TikTok"),
        ("tumblr", "Tumblr"),
        ("twitch", "Twitch"),
        ("twitter", "Twitter"),
        ("website", "Website"),
        ("whatsapp", "WhatsApp"),
        ("youtube", "YouTube"),
        ("other", "Other"),
    ]
    url_type = models.CharField(max_length=20, choices=URL_CHOICES, default="other")
    brand = models.ForeignKey(Brand, related_name="links", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    url = models.URLField()
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    clicks_count = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.title} - {self.clicks_count} clicks"


class PageView(models.Model):
    brand = models.ForeignKey(
        Brand, on_delete=models.CASCADE, related_name="page_views"
    )
    ip_address = models.GenericIPAddressField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-timestamp"]
