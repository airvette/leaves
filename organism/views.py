# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from datetime import datetime

# Create your views here.


def index(request):
    datetime_accessed = datetime.now()
    date_accessed = datetime_accessed.date()
    time_accessed = datetime_accessed.time()
    date_format = '%a, %b %d, %Y'
    time_format = '%I:%M %p'
    context = {
        'message': 'Here is a test page.',
        'date_accessed': date_accessed.strftime(date_format),
        'time_accessed': time_accessed.strftime(time_format)
    }
    return render(request, 'organism/index.html', context)
