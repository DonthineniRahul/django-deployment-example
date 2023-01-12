import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','rahul.settings')

import django
django.setup()

import random
from virat.models import Day,Night,MidDay
from faker import Faker

fakegen = Faker()
night = ['dark','full_moon','half_moon']

def add_night():
	t = Topic.objects.get_or_create(name=random.choice(night))[0]
	t.save()
	return t