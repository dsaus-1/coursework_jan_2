import random

from django.conf import settings
from django.core.cache import cache

from blog.models import Blog


def cache_home_page_all():
    queryset = Blog.objects.filter(publication_status=Blog.STATUS_ACTIVE)
    if settings.CACHE_ENABLED:
        key = f'cache_home_page_all'
        cache_data = cache.get(key)

        if cache_data is None:
            cache_data = queryset
            cache.set(key, cache_data)

        return cache_data
    return queryset

def random_publication(data):
    cache_home_page = [item[0] for item in data.values_list('id')]
    random.shuffle(cache_home_page)
    number_publication = 3

    if len(cache_home_page) < 3:
        number_publication = len(cache_home_page)

    publication = [data.filter(id=cache_home_page[n]) for n in range(number_publication)]

    return publication
