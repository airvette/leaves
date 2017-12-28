# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import validate_comma_separated_integer_list
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Entity(models.Model):
    name = models.CharField(max_length=30)
    # TODO: make picture_path = models.CharField()
    entity_type = models.CharField(
        max_length=20,
        default='entity'
    )
    ''' ^^ animal, plant, fungi, bacteria (includes archaea) or inanimate
    (sun, water, etc)'''

    foods_eaten = models.CharField(
        validators=[validate_comma_separated_integer_list],
        max_length=40,
        default=''
    )

    def __str__(self):
        return self.name
