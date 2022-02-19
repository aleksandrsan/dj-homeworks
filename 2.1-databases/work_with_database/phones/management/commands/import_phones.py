import csv

from django.core.management.base import BaseCommand
from django.template.defaultfilters import slugify
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):

        #delete old data
        Phone.objects.all().delete()

        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            el_phone = Phone(name=phone['name'], image=phone['image'], price=int(phone['price']), release_date=phone['release_date'],
                             lte_exists=phone['lte_exists'], slug=slugify(phone['name']))
            el_phone.save()
