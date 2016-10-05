# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from app.pet.models import Vaccine, Pet
# Register your models here.

admin.site.register(Vaccine)
admin.site.register(Pet)