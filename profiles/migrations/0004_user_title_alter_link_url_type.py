# Generated by Django 5.1.5 on 2025-01-20 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_link_url_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='title',
            field=models.CharField(default='My Linktree', max_length=255),
        ),
        migrations.AlterField(
            model_name='link',
            name='url_type',
            field=models.CharField(choices=[('facebook', 'Facebook'), ('instagram', 'Instagram'), ('linkedin', 'LinkedIn'), ('pinterest', 'Pinterest'), ('reddit', 'Reddit'), ('snapchat', 'Snapchat'), ('spotify', 'Spotify'), ('tiktok', 'TikTok'), ('tumblr', 'Tumblr'), ('twitch', 'Twitch'), ('twitter', 'Twitter'), ('website', 'Website'), ('whatsapp', 'WhatsApp'), ('youtube', 'YouTube'), ('other', 'Other')], default='other', max_length=20),
        ),
    ]
