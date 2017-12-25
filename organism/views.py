# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        'message': 'This is a test post on the index page'
    }
    return render(request, 'organism/index.html', context)
