from contacts.models import Contact, User
from django.db.models import Count, Q
from django.utils.timezone import now
from datetime import timedelta
from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_email_each_day():
    contact_user_counts = Contact.objects.filter(
        Q(created_at__date=now()) | Q(created_at=now() - timedelta(days=1))

    ).values("user").annotate(
        total=Count(
            "user"
        )
    )

    for contact_user_count in contact_user_counts:
        user = User.objects.get(id=contact_user_count["user"])
        send_mail(
            'Your contacts',
            f'{Contact.objects.filter(user=user)}.',
            'from@example.com',
            [f'{user.email}'],
            fail_silently=False,
        )
    return "done"
