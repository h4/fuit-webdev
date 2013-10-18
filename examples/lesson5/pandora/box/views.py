# encoding=utf-8

from django.shortcuts import render
from .models import Thing


def list(request):
	things = Thing.objects.order_by('title')
	context = {
		"things": things
	}

	return render(request, 'list.html', context)
