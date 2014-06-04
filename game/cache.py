from django.core.cache import cache
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from models import Level

ALL_LEVELS_KEY = "model_all_levels"

@receiver(post_save, sender=Level)
@receiver(post_delete, sender=Level)
def clear_level_cache(sender, **kwargs):
    print "Clearing cache"
    cache.delete(ALL_LEVELS_KEY)

def cached_all_levels():
    result = cache.get(ALL_LEVELS_KEY)
    if result is None:
        result = Level.objects.filter(default=True).order_by('id')
        print "set cache"
        cache.set(ALL_LEVELS_KEY, result)
    return result

