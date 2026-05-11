from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from datetime import timedelta
from links.models import Link

@receiver(post_save, sender=Link)
def delete_old_links(sender, instance, created, **kwargs):

    threshold_date = timezone.now() - timedelta(days=30)

    old_active_links = Link.objects.filter(
        created_at__lte=threshold_date,
    )
    count = old_active_links.delete()[0]

    if count > 0:
        print(f'Deleted {count} old links')

