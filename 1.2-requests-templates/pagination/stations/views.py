import csv

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):

    page_number = int(request.GET.get("page", 1))
    pagi_step = 20

    paginator = Paginator(stations, pagi_step)
    page = paginator.get_page(page_number)

    context = {
         'bus_stations': page.object_list,
         'page': page,
    }
    return render(request, 'stations/index.html', context)


# init    stations   from csv
stations = []

with open(settings.BUS_STATION_CSV, newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        stations.append({'Name': row[1], 'Street': row[4], 'District': row[6]})
