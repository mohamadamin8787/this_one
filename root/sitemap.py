from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from services.models import Services


class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = "daily"

    def items(self):
        return [
            'root:home',
            'root:about',
            'root:contact',
            'services:service'
        ]

    def location(self, item):
        return reverse(item)

class DynamicViewSitemap(Sitemap):
    priority = 0.5
    changefreq = "daily"

    def items(self):
        return Services.objects.all()
            
       

    def location(self, obj):
        return 'services/detail%i'%obj.id
