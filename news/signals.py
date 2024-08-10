from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.urls import reverse
from django.conf import settings
from .models import Post, Subscriber


@receiver(post_save, sender=Post)
def news_notification(sender, instance, created, **kwargs):
    if created:
        subject = "This Week's News!"
        unsubscribe_url = f"{settings.SITE_URL}{reverse('unsubscribe')}?email={{email}}"
        message = (
            f'A new article "{instance.title}" has been published. Check it out at {instance.get_absolute_url()}.\n\n'
            f'If you wish to unsubscribe from our newsletter, click here: {unsubscribe_url}'
        )
        subscribers = Subscriber.objects.all()
        for subscriber in subscribers:
            send_mail(
                subject,
                message.format(email=subscriber.email),
                'davidwebtesting@gmail.com',
                [subscriber.email],
                fail_silently=False,
            )