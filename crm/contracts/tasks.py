import datetime

from celery import shared_task

from .models import Contract


@shared_task
def archive_expired_contracts():
    now = datetime.datetime.now(datetime.UTC)
    Contract.objects.filter(end_date__lte=now).update(archived=Contract.Status.ARCHIVED)
